#!/bin/bash
set -euo pipefail

python -m black --no-color --diff --check --quiet .

