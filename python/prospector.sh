#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

# Prospector is really slow for some reason scanning a repo with a lot of files.
# So use find and xargs to run it.
find . -name "*.py" | xargs python -m prospector -M

