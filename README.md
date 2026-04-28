# My UV Package Creator

A simple Python CLI tool that lets you create a new package/project directory directly from the Linux terminal using a single command.

After installation, you can run:

```bash
create my_project
```

and it will create:

```text
./my_project
```

in your current working directory.

---

# Features

- Simple terminal command
- Creates folders instantly
- Works from any directory
- Built with Python
- Uses modern `uv` package management
- Supports editable development installs

---

# Requirements

- Python 3.9+
- Linux/macOS
- `uv` installed (recommended)

Optional:
- `pip`

---

# Install UV

Install `uv`:

## Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

---

# Project Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd my-uvpackage-creator
```

---

# Create Virtual Environment

```bash
uv venv
```

This creates:

```text
.venv/
```

---

# Activate Virtual Environment

## Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
uv sync
```

This installs all project dependencies from `pyproject.toml`.

---

# Alternative Installation Using pip

If you prefer using `pip` instead of `uv`:

```bash
pip install -e .
```

The `-e` flag installs the package in editable/development mode.

This means:
- code changes update immediately
- no reinstall required after edits

---

# Usage

Once installed, you can create a directory from anywhere in the terminal.

## Syntax

```bash
create "package_name"
```

or

```bash
create package_name
```

---

# Examples

## Create a package folder

```bash
create my_app
```

Creates:

```text
./my_app
```

---

## Create inside another directory

```bash
cd ~/Desktop/projects

create test_package
```

Creates:

```text
~/Desktop/projects/test_package
```

---

# Example Workflow

```bash
mkdir demo
cd demo

create my_library
```

Result:

```text
demo/
└── my_library/
```

---

# Development

## Run locally

```bash
python -m my_uvpackage_creator.cli my_project
```

---

# Editable Development Mode

Recommended for contributors:

```bash
pip install -e .
```

or

```bash
uv sync
```

---

# Project Structure

```text
my-uvpackage-creator/
├── pyproject.toml
├── README.md
├── my_uvpackage_creator/
│   ├── __init__.py
│   └── cli.py
└── .venv/
```

---

# How It Works

The package exposes a terminal command using Python entry points.

In `pyproject.toml`:

```toml
[project.scripts]
create = "my_uvpackage_creator.cli:main"
```

This maps:

```bash
create
```

to:

```python
main()
```

inside:

```text
my_uvpackage_creator/cli.py
```

---

# Troubleshooting

## Command not found: create

Ensure the package is installed:

```bash
pip install -e .
```

or

```bash
uv sync
```

Then restart the terminal.

---

## Virtual environment not activated

Activate it manually:

```bash
source .venv/bin/activate
```

---

## Permission denied

Ensure Python and uv are installed correctly.

You may also need:

```bash
chmod +x <script>
```

---

# Uninstall

```bash
pip uninstall my-uvpackage-creator
```

---

# Future Improvements

- Auto-generate Python package structure
- Add template support
- Create README automatically
- Git initialization
- License generation
- pyproject.toml scaffolding

---

# License

MIT License

---

# Author

Built using Python and uv.
