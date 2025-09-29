#!/bin/bash
set -euo pipefail

# Prospector is really slow for some reason scanning a repo with a lot of files.
find . -not \( -path "*.terraform" -prune -or -path "*venv" -prune -or -path "*node_modules" -prune \) -name "*.py" -exec python -m prospector -M {} +

