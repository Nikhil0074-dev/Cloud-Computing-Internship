"""Small reusable functions used by main.py."""
from datetime import datetime


def build_greeting(name: str) -> str:
    """Return a greeting for the given name."""
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {name}! Welcome to my internship journey!"


def day_of_week(date: datetime | None = None) -> str:
    """Return the day name, e.g. 'Thursday'."""
    date = date or datetime.now()
    return date.strftime("%A")


def add_numbers(a: float, b: float) -> float:
    """Add two numbers. Used to practice testing."""
    return a + b
