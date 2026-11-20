"""Command line interface. Run: python -m skilltracker --help"""
import argparse
import os

from . import quiz, storage, tracker

DATA_FILE = os.path.join("data", "progress.json")
QUIZ_FILE = os.path.join("data", "quiz_questions.json")


def build_parser():
    p = argparse.ArgumentParser(prog="skilltracker", description="Track your learning progress.")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("add-concept", help="Add a concept and why it matters")
    a.add_argument("name")
    a.add_argument("why")

    a = sub.add_parser("practice", help="Log a practice session")
    a.add_argument("concept")
    a.add_argument("note")
    a.add_argument("minutes", type=int)

    a = sub.add_parser("add-project", help="Add a small project for a concept")
    a.add_argument("name")
    a.add_argument("concept")

    a = sub.add_parser("feedback", help="Add mentor feedback")
    a.add_argument("text")

    a = sub.add_parser("fix-feedback", help="Mark feedback as fixed")
    a.add_argument("number", type=int)

    sub.add_parser("quiz", help="Take the self-assessment quiz")
    sub.add_parser("summary", help="Show progress summary")
    return p


def run_quiz():
    questions = quiz.load_questions(QUIZ_FILE)
    answers = []
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['question']}")
        for n, opt in enumerate(q["options"], 1):
            print(f"  {n}. {opt}")
        while True:
            raw = input("Your answer: ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(q["options"]):
                answers.append(int(raw) - 1)
                break
            print("Please type a valid option number.")
    correct, weak = quiz.score(questions, answers)
    print(f"\nScore: {correct}/{len(questions)}")
    if weak:
        print("Study these topics again: " + ", ".join(weak))
    else:
        print("No weak topics. Good.")


def main(argv=None):
    args = build_parser().parse_args(argv)
    data = storage.load(DATA_FILE)
    try:
        if args.command == "add-concept":
            tracker.add_concept(data, args.name, args.why)
        elif args.command == "practice":
            tracker.log_practice(data, args.concept, args.note, args.minutes)
        elif args.command == "add-project":
            tracker.add_project(data, args.name, args.concept)
        elif args.command == "feedback":
            tracker.add_feedback(data, args.text)
        elif args.command == "fix-feedback":
            tracker.mark_feedback_fixed(data, args.number)
        elif args.command == "quiz":
            run_quiz()
            return 0
        elif args.command == "summary":
            for key, value in tracker.summary(data).items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            return 0
    except ValueError as err:
        print(f"Error: {err}")
        return 1
    storage.save(DATA_FILE, data)
    print("Saved.")
    return 0
