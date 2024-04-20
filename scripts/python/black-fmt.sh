#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

python -m black --no-color --diff --check --quiet .

