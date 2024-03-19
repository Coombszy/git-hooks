#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

find . -not \( -path "*.terraform" -prune \) -name "*.sh" -exec shellcheck --color=never {} +

