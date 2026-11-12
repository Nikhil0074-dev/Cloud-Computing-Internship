"""Entry point: the Hello World program."""
from src.utils import build_greeting, day_of_week


def main() -> None:
    print("Hello World!")
    print("Welcome to my internship journey!")
    print(build_greeting("Intern"))
    print(f"Today is {day_of_week()}.")


if __name__ == "__main__":
    main()
