#!/bin/bash

# Is tflint installed?
if ! [ -x "$(command -v tflint)" ]; then
  echo 'Error: tflint is not installed.' >&2
  exit 1
fi

# Run tflint
tflint --no-color --recursive

