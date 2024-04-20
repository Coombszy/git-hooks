#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

find . -not \( -path "*.terraform" -prune -or -path "*node_modules" -prune \) -name "*.sh" -exec shellcheck --color=never {} +

