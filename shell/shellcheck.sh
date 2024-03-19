#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

find . -name "*.sh" | xargs shellcheck --color=never

