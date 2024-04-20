#!/bin/bash
# Copyright (C) 2024  Coombszy
set -euo pipefail

terraform fmt -recursive -check -no-color -diff

