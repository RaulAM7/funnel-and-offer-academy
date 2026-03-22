#!/usr/bin/env python3
"""Build a first-pass Excalidraw canvas from an Academy block summary + extraction."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import textwrap
import unicodedata
from pathlib import Path


CANVAS_WIDTH = 2440
BANNER_X = 80
BANNER_Y = 80
BANNER_W = 2280
BANNER_H = 110
FRAME_Y_1 = 250
FRAME_Y_2 = 490
BOTTOM_Y = 760
CARD_W = 660
CARD_H = 180
CARD_GAP = 90


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text).strip().lower()


def clean_md(text: str) -> str:
    text = text.replace("`", "")
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def stable_int(*parts: object, limit: int = 2_000_000_000) -> int:
    raw = "::".join(str(part) for part in parts)
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()
    return int(digest[:12], 16) % limit


def make_id(prefix: str, *parts: object) -> str:
    digest = hashlib.md5("::".join(str(part) for part in parts).encode("utf-8")).hexdigest()
    return f"{prefix}_{digest[:10]}"


def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = normalize(line[3:])
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line.rstrip())
    return sections


def split_subsections(lines: list[str]) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if current_heading is not None:
                sections.append((clean_md(line_cleanup(current_heading)), current_lines))
            current_heading = line[4:].strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((clean_md(line_cleanup(current_heading)), current_lines))
    return sections


def line_cleanup(text: str) -> str:
    return text.replace("--", "-")


def list_items(lines: list[str], numbered: bool = False) -> list[str]:
    items: list[str] = []
    pattern = r"^\d+\.\s+" if numbered else r"^-+\s+"
    for line in lines:
        if re.match(pattern, line.strip()):
            item = re.sub(pattern, "", line.strip())
            items.append(clean_md(item))
    return items


def parse_frameworks(summary_sections: dict[str, list[str]]) -> list[dict[str, str]]:
    raw_items = list_items(summary_sections.get(normalize("Frameworks introducidos"), []), numbered=True)
    frameworks: list[dict[str, str]] = []
    for item in raw_items:
        title = item
        body = ""
        if " -- " in item:
            title, body = item.split(" -- ", 1)
        elif " - " in item:
            title, body = item.split(" - ", 1)
        elif ": " in item:
            title, body = item.split(": ", 1)
        frameworks.append(
            {
                "title": clean_md(title).strip(),
                "body": clean_md(body).strip(),
            }
        )
    return frameworks


def parse_takeaways(summary_sections: dict[str, list[str]]) -> list[str]:
    return list_items(summary_sections.get(normalize("Takeaways clave"), []), numbered=False)


def parse_patterns(extraction_sections: dict[str, list[str]]) -> list[str]:
    subsection_lines = extraction_sections.get(normalize("Patrones"), [])
    patterns: list[str] = []
    for heading, lines in split_subsections(subsection_lines):
        details = list_items(lines, numbered=False)
        detail = details[0] if details else ""
        value = heading
        if detail:
            value = f"{heading}: {detail}"
        patterns.append(clean_md(value))
    return patterns[:4]


def parse_limits(extraction_sections: dict[str, list[str]]) -> list[str]:
    subsection_lines = extraction_sections.get(normalize("Limites y Dudas"), [])
    limits: list[str] = []
    for heading, lines in split_subsections(subsection_lines):
        details = list_items(lines, numbered=False)
        detail = details[0] if details else ""
        value = heading
        if detail:
            value = f"{heading}: {detail}"
        limits.append(clean_md(value))
    return limits[:4]


def wrap_text(text: str, width: int) -> str:
    if not text:
        return ""
    lines = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    return "\n".join(lines)


def text_size(text: str, font_size: int, max_width: int) -> tuple[float, float]:
    lines = text.splitlines() or [""]
    longest = max(len(line) for line in lines)
    width = min(max_width, max(140, longest * font_size * 0.56))
    height = max(font_size * 1.35, len(lines) * font_size * 1.35)
    return round(width, 2), round(height, 2)


def base_element(element_id: str, element_type: str) -> dict[str, object]:
    return {
        "type": element_type,
        "version": 1,
        "versionNonce": stable_int(element_id, "nonce"),
        "isDeleted": False,
        "id": element_id,
        "fillStyle": "hachure",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "angle": 0,
        "seed": stable_int(element_id, "seed"),
        "groupIds": [],
        "frameId": None,
        "updated": 0,
        "link": None,
        "locked": False,
    }


def rectangle(element_id: str, x: float, y: float, width: float, height: float, stroke: str, fill: str) -> dict[str, object]:
    element = base_element(element_id, "rectangle")
    element.update(
        {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "strokeColor": stroke,
            "backgroundColor": fill,
            "roundness": {"type": 3},
            "boundElements": [],
        }
    )
    return element


def text_element(element_id: str, x: float, y: float, text: str, font_size: int, color: str, max_width: int) -> dict[str, object]:
    wrapped = wrap_text(text, width=max(18, int(max_width / (font_size * 0.56))))
    width, height = text_size(wrapped, font_size, max_width)
    element = base_element(element_id, "text")
    element.update(
        {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "roundness": None,
            "boundElements": None,
            "fontSize": font_size,
            "fontFamily": 1,
            "text": wrapped,
            "rawText": wrapped,
            "originalText": wrapped,
            "textAlign": "left",
            "verticalAlign": "top",
            "containerId": None,
            "lineHeight": 1.35,
            "autoResize": False,
        }
    )
    return element


def panel(elements: list[dict[str, object]], key: str, x: float, y: float, width: float, height: float, title: str, body: str, fill: str) -> None:
    rect_id = make_id("rect", key)
    title_id = make_id("text", key, "title")
    body_id = make_id("text", key, "body")
    elements.append(rectangle(rect_id, x, y, width, height, "#1f2937", fill))
    elements.append(text_element(title_id, x + 24, y + 20, title, 24, "#111827", int(width - 48)))
    elements.append(text_element(body_id, x + 24, y + 64, body, 16, "#1f2937", int(width - 48)))


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_canvas(summary_path: Path, extraction_path: Path, output_path: Path, title_override: str | None) -> None:
    summary_text = summary_path.read_text(encoding="utf-8")
    extraction_text = extraction_path.read_text(encoding="utf-8")

    summary_sections = split_sections(summary_text)
    extraction_sections = split_sections(extraction_text)

    frameworks = parse_frameworks(summary_sections)
    takeaways = parse_takeaways(summary_sections)[:5]
    patterns = parse_patterns(extraction_sections)
    limits = parse_limits(extraction_sections)

    block_title_match = re.search(r"^#\s+(.*)$", summary_text, re.MULTILINE)
    block_title = clean_md(block_title_match.group(1)) if block_title_match else summary_path.stem
    title = title_override or block_title

    subtitle_bits = [
        f"{len(frameworks)} frameworks",
        f"{len(takeaways)} takeaways",
        "MCP-first draft",
    ]
    subtitle = " | ".join(subtitle_bits)

    elements: list[dict[str, object]] = []
    panel(
        elements,
        "banner",
        BANNER_X,
        BANNER_Y,
        BANNER_W,
        BANNER_H,
        title,
        subtitle,
        "#e9f5ff",
    )

    framework_colors = ["#dbeafe", "#fef3c7", "#dcfce7", "#fde2e7", "#ede9fe"]
    framework_positions = [
        (80, FRAME_Y_1),
        (830, FRAME_Y_1),
        (1580, FRAME_Y_1),
        (80, FRAME_Y_2),
        (830, FRAME_Y_2),
    ]

    for index, framework in enumerate(frameworks[:5]):
        x, y = framework_positions[index]
        body = framework["body"] or "Framework fundacional del bloque."
        panel(
            elements,
            f"framework-{index}",
            x,
            y,
            CARD_W,
            CARD_H,
            framework["title"],
            body,
            framework_colors[index % len(framework_colors)],
        )

    panel(
        elements,
        "takeaways",
        1580,
        FRAME_Y_2,
        CARD_W,
        390,
        "Takeaways clave",
        bullets(takeaways or ["Sin takeaways detectados en el resumen."]),
        "#fff7ed",
    )

    panel(
        elements,
        "patterns",
        80,
        BOTTOM_Y,
        1080,
        380,
        "Patrones para recordar",
        bullets(patterns or ["Sin patrones estructurados detectados en la extraccion."]),
        "#eefbf3",
    )

    panel(
        elements,
        "limits",
        1240,
        BOTTOM_Y,
        1000,
        380,
        "Riesgos y tensiones",
        bullets(limits or ["Sin limites estructurados detectados en la extraccion."]),
        "#fff1f2",
    )

    note_body = (
        f"Origen semantico: {summary_path.name} + {extraction_path.name}\n"
        "Si el MCP esta disponible, este canvas se refina en vivo.\n"
        "Si no, este archivo funciona como draft editable en Antigravity."
    )
    panel(
        elements,
        "note",
        1580,
        250,
        CARD_W,
        180,
        "Uso previsto",
        note_body,
        "#f3f4f6",
    )

    scene = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "gridSize": 20,
            "gridStep": 5,
            "gridModeEnabled": False,
            "viewBackgroundColor": "#ffffff",
            "theme": "light",
            "zoom": {"value": 0.54},
            "scrollX": 0,
            "scrollY": 0,
        },
        "files": {},
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(scene, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--extraction", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--title", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_canvas(args.summary, args.extraction, args.output, args.title)


if __name__ == "__main__":
    main()
