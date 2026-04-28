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



# Future Improvements

- Auto-generate Python package structure
- Add template support
- Create README automatically
- Git initialization
- License generation
- pyproject.toml scaffolding

# Author

Built using Python and uv.
