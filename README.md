# git-hooks

This repository provides a configurable git hooks system with support for multiple languages and tools. The hooks are dynamically configured based on file types detected in your repository.

## Features

- **Configurable targets**: Enable/disable hooks for different languages and tools
- **Automatic file type detection**: Hooks only run when relevant files are detected
- **Parallel execution**: Scripts run concurrently for better performance
- **Multi-language support**: Python, Rust, Terraform, Shell, CloudFormation, and Git
- **Local repository integration**: Automatically detects and runs local pre-commit configurations (e.g., npm husky)

## Installation

To install the hooks, run the following command from the root of the repository:

```bash
git config --global core.hooksPath "$(pwd)/hooks"
```

## Configuration

The hooks are configured via `config/config.json`. If this file doesn't exist, it will be created automatically from `config/config.json.example` on first run.

**By default, all language/tool targets are disabled except Git hooks.** You need to explicitly enable the tools you want to use by setting `"enabled": true` in your configuration file.

## Supported Tools & Requirements

All tools must be available on the `PATH`:

- **Python**:
  - [Black](https://github.com/psf/black) - Code formatting
  - [Prospector](https://prospector.landscape.io/en/master/) - Static analysis
- **Terraform**:
  - [Terraform](https://www.terraform.io/) - Infrastructure as code
  - [TFLint](https://github.com/terraform-linters/tflint) - Terraform linting
- **Rust**:
  - [Rustfmt](https://github.com/rust-lang/rustfmt) - Code formatting (included with cargo)
  - [Clippy](https://github.com/rust-lang/rust-clippy) - Linting (included with cargo)
- **CloudFormation**:
  - [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) - CloudFormation template validation
- **Shell**:
  - [ShellCheck](https://github.com/koalaman/shellcheck) - Shell script analysis
