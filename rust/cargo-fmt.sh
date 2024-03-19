#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

cargo fmt --all --check -- --color never

