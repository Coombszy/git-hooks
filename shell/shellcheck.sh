#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

find . -name "*.sh" -exec shellcheck --color=never {} +

