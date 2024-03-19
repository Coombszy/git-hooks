#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

# Capture output and store stdout and stderr in separate variables
if ! cargo clippy --color never --all -- -D warnings 2>&1 | tee clippy_output.txt
then
    cat clippy_output.txt
    # Delete output file if no errors
    rm clippy_output.txt
    exit 1
fi

# Delete output file if no errors
rm clippy_output.txt

