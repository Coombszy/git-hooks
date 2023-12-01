#!/bin/bash
set -euo pipefail

cargo fmt --all --check -- --color never

