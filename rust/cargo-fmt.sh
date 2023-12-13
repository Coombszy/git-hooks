#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

cargo fmt --all --check -- --color never

