from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Folder name")
    args = parser.parse_args()
    folder_path = Path.cwd() / args.name
    folder_path.mkdir(exist_ok=True)
    print(f"Created folder: {folder_path}")
