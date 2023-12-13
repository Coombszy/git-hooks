#!/bin/bash
# Copyright (C) 2023  Coombszy
set -euo pipefail

terraform fmt -recursive -check -no-color -diff

