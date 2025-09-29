#!/bin/bash
set -euo pipefail

# Find CloudFormation template files that contain AWSTemplateFormatVersion, excluding files with "packaged" in the name
files=$(find . -type f \( -name "*.yaml" -o -name "*.yml" -o -name "*.json" \) ! -name "*packaged*" -print \
  | xargs grep -0 -l "AWSTemplateFormatVersion" || true)

if [ -n "$files" ]; then
  cfn-lint --format parseable "$files"
fi
