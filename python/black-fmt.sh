#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

python -m black --no-color --diff --check --quiet .

