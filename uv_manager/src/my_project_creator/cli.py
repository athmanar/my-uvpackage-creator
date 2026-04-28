from pathlib import Path
import argparse
from urllib.error import URLError
from urllib.request import urlopen


APACHE_LICENSE_URL = "https://www.apache.org/licenses/LICENSE-2.0.txt"


def _get_apache_license_text() -> str:
    try:
        with urlopen(APACHE_LICENSE_URL, timeout=10) as response:
            return response.read().decode("utf-8")
    except (URLError, TimeoutError, UnicodeDecodeError):
        local_license = Path(__file__).resolve().parents[2] / "LICENSE"
        if local_license.exists():
            return local_license.read_text(encoding="utf-8")
        return "Apache License 2.0\n\nhttps://www.apache.org/licenses/LICENSE-2.0"


def main():
    parser = argparse.ArgumentParser(description="Create a UV package scaffold with pyproject.toml and src layout.")
    parser.add_argument("name", help="Project/folder name (also used as package name)")
    args = parser.parse_args()

    project_name = args.name.strip()
    package_name = project_name.replace("-", "_").replace(" ", "_")

    project_dir = Path.cwd() / project_name
    src_package_dir = project_dir / "src" / package_name

    # Create directories
    src_package_dir.mkdir(parents=True, exist_ok=True)

    pyproject_content = f"""# ============================================================================ #
# BUILD SYSTEM CONFIGURATION                                                   #
# ============================================================================ #
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/{package_name}"]

# ============================================================================ #
# PROJECT CONFIGURATION                                                        #
# ============================================================================ #
[project]
name = "{package_name}"
version = "0.1.0"
requires-python = ">=3.12"
description = "A package for creating folder structure for ne uv packages"
license = {{ file = "LICENSE" }}
authors = [{{ name = "Athma Narayanan" }}]
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3.12",
]

[project.scripts]
create = "{package_name}.cli:main"
"""

    init_content = """__version__ = "0.1.0"
"""

    cli_content = f"""import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="{package_name}", help="Name to print")
    args = parser.parse_args()
    print(f"Hello from {{args.name}}")
"""

    license_content = _get_apache_license_text()

    # Write files
    (project_dir / "pyproject.toml").write_text(pyproject_content, encoding="utf-8")
    # Also created as requested ("project.toml")
    (project_dir / "project.toml").write_text(pyproject_content, encoding="utf-8")
    (src_package_dir / "__init__.py").write_text(init_content, encoding="utf-8")
    (src_package_dir / "cli.py").write_text(cli_content, encoding="utf-8")
    (project_dir / "LICENSE").write_text(license_content, encoding="utf-8")

    print(f"Created UV project scaffold at: {project_dir}")

