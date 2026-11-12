"""Prints the version of each tool. Run it and screenshot the output as evidence.

Usage:  python scripts/check_setup.py
"""
import shutil
import subprocess
import sys

TOOLS = {
    "Python": [sys.executable, "--version"],
    "Git": ["git", "--version"],
    "Node.js (optional)": ["node", "--version"],
    "npm (optional)": ["npm", "--version"],
    "VS Code (optional)": ["code", "--version"],
}


def main() -> None:
    print("=== Setup check ===")
    for name, cmd in TOOLS.items():
        if cmd[0] != sys.executable and shutil.which(cmd[0]) is None:
            print(f"[MISSING] {name}")
            continue
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, check=True)
            first_line = (out.stdout or out.stderr).strip().splitlines()[0]
            print(f"[OK]      {name}: {first_line}")
        except Exception as err:  # noqa: BLE001
            print(f"[ERROR]   {name}: {err}")


if __name__ == "__main__":
    main()
