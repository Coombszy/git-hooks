# git-hooks

This repository is to act as a dumping ground for git hooks that I use and create over time.

## Installation

To install the hooks, simply run the following command from the root of the repository:

```bash
git config --global core.hooksPath "$(pwd)/hooks"
```

## Requirements
Some of the hooks require additional software to be installed. These are listed below. All must be available on the `PATH`.

- `pre-commit`:
  - Terraform: 
    - [Terraform](https://www.terraform.io/)
    - [TFLint](https://github.com/terraform-linters/tflint)
  - Python:
    - [Black](https://github.com/psf/black)
    - [Prospector](https://prospector.landscape.io/en/master/)
  - Rust:
    - [Rustfmt](https://github.com/rust-lang/rustfmt) - included with cargo
    - [Clippy](https://github.com/rust-lang/rust-clippy) - included with cargo
