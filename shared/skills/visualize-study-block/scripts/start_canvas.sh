#!/usr/bin/env bash
set -euo pipefail

container_name="${EXCALIDRAW_CANVAS_NAME:-academy-excalidraw-canvas}"
host_port="${EXCALIDRAW_CANVAS_PORT:-3000}"

running_name="$(docker ps --filter "name=^/${container_name}$" --format '{{.Names}}')"
if [ "${running_name}" = "${container_name}" ]; then
  echo "Excalidraw canvas already running at http://localhost:${host_port}"
  exit 0
fi

existing_name="$(docker ps -a --filter "name=^/${container_name}$" --format '{{.Names}}')"
if [ "${existing_name}" = "${container_name}" ]; then
  docker start "${container_name}" >/dev/null
  echo "Excalidraw canvas started at http://localhost:${host_port}"
  exit 0
fi

docker run -d -p "${host_port}:3000" --name "${container_name}" ghcr.io/yctimlin/mcp_excalidraw-canvas:latest >/dev/null
echo "Excalidraw canvas started at http://localhost:${host_port}"
