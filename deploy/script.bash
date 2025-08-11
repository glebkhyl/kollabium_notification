#!/bin/bash

set -e

echo "[DEPLOY] Restart Docker Compose file"
docker compose stop
docker compose up -d --build 

echo "[DEPLOY] All done now"
