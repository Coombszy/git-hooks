#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

find . -name "*.sh" -exec shellcheck --color=never {} +

