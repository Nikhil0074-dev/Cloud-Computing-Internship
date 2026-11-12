# Task 1- Internship Project Fundamentals and Setup

A small Python project that proves my development environment works:
Python, Git, GitHub, a clean project structure, tests, and a Hello World program.

## What is inside

| Path | Purpose |
| --- | --- |
| `src/main.py` | Entry point. Prints Hello World. |
| `src/utils.py` | Reusable functions. |
| `tests/` | Automatic tests. |
| `scripts/check_setup.py` | Prints versions of installed tools. |
| `docs/` | Setup report, learning list, Git cheat sheet, checklist. |
| `requirements.txt` | Python packages needed (none right now). |
| `.gitignore` | Files Git should not track. |

## Requirements

- Python 3.10 or newer
- Git

## How to run

```bash
python -m src.main
```

Expected output:

```
Hello World!
Welcome to my internship journey!
Hello, Intern! Welcome to my internship journey!
Today is <day name>.
```

## How to test

```bash
python -m unittest discover -s tests -v
```

## How to check your setup

```bash
python scripts/check_setup.py
```



## Author
Name- https://github.com/Nikhil0074-dev/