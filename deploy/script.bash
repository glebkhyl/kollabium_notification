#!/bin/bash

set -e

echo "[DEPLOY] Restart Docker Compose file"
docker compose stop
docker compose up -d

echo "[DEPLOY] All done now"
