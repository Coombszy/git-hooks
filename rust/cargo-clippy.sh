#!/bin/bash
set -euo pipefail

# Capture output and store stdout and stderr in separate variables
cargo clippy --color never --all -- -D warnings 2>&1 | tee clippy_output.txt

# If exit code is not 0, print output and exit
if [ $? -ne 0 ]; then
    cat clippy_output.txt
    # Delete output file if no errors
    rm clippy_output.txt
    exit 1
fi

# Delete output file if no errors
rm clippy_output.txt

