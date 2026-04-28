# My UV Package Creator

A simple Python CLI tool that lets you create a new package/project directory directly from the Linux terminal using a single command.
After installation, you can run:

```bash
create my_project
```

and it will create:

```text
.
└── my_project/
	├── LICENSE
	├── pyproject.toml
	├── project.toml
	└── src/
		└── my_project/
			├── __init__.py
			└── cli.py
```

in your current working directory.

---

# Features

- Simple terminal command
- Creates a full UV package scaffold instantly
- Works from any directory
- Built with Python
- Uses modern `uv` package management
- Supports editable development installs
- Generates `pyproject.toml`, `project.toml`, and `LICENSE`
- Creates `src/<package_name>/__init__.py` and `src/<package_name>/cli.py`
- Pulls Apache 2.0 license text automatically (with local fallback)

---

# Requirements

- Python 3.12+
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

---

# Project Setup

Clone the repository:

```bash
git clone https://github.com/athmanar/my-uvpackage-creator.git
cd my-uvpackage-creator
```

---

# Create Virtual Environment

```bash
uv venv
```

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


---

# Usage

Once installed, you can create project directory from anywhere in the terminal.

## Syntax

```bash
create "package_name"
```

or

```bash
create package_name
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
├── LICENSE
├── pyproject.toml
├── project.toml
└── src/test_package/
```

---

# Example Workflow

```bash
mkdir demo
cd demo

create my_library
```


---

# Development

## Run locally

```bash
python -m my_project_creator.cli my_project
```
---



# Future Improvements

- Auto-generate Python package structure
- Add template support
- Create README automatically
- Git initialization
- Add test scaffolding

# Author

Built using Python and uv.
