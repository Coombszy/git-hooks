#!/bin/bash
set -euo pipefail

terraform fmt -recursive -check -no-color -diff

