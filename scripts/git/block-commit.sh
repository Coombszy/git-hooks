#!/bin/bash
set -euo pipefail

# Script will block commit if any of the staged files contain any variation of [`BLOCK-COMMIT`, `BLOCK_COMMIT`, `BLOCK COMMIT`]

# List of files to skip from block commit check
#               v--itself          v--example config file
files_to_skip=("block-commit.sh" "config.json.example")

# Get the list of staged files
staged_files=$(git diff --cached --name-only)

# if there are no staged files, exit
if [ -z "$staged_files" ]
then
  exit 0
fi

# Remove any deleted files from the staged files list
staged_files=$(echo "$staged_files" | xargs -I {} git ls-files {})

# Create empty array to store files that contain block commit message
block_commit_files=()

# Create function to return filename from path
get_filename() {
  basename "$1"
}

# Loop through the staged files
for file in $staged_files
do
  # Get the filename from the path and see if it is in the files to skip list
  # If it is, skip the file
  if [[ ${files_to_skip[*]} =~ $(get_filename "$file") ]]
  then
    continue
  fi

  # Check if the file contains any variation of [`BLOCK-COMMIT`, `block-commit`, `BLOCK COMMIT`]
  if grep -q -i -E 'BLOCK-COMMIT|BLOCK_COMMIT|BLOCK COMMIT' "$file"
  then
    # Add the file to the block commit files array
    block_commit_files+=("$file")
  fi
done

# If the block commit files array is not empty, print the files and exit with a non-zero status
# This will block the commit
if [ ${#block_commit_files[@]} -gt 0 ]
then
  echo "The following contain a block str: (BLOCK-COMMIT, BLOCK_COMMIT, BLOCK COMMIT)"
  for file in "${block_commit_files[@]}"
  do
    echo "$file"
  done
  exit 1
fi
