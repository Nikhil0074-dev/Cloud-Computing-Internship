"""Quiz and self-assessment: find weak topics."""
import json


def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def score(questions, answers):
    """answers is a list of chosen option numbers (0-based), one per question.

    Returns (correct_count, weak_topics) where weak_topics lists topics
    that were answered wrong.
    """
    if len(answers) != len(questions):
        raise ValueError("Give one answer per question.")
    correct = 0
    weak = []
    for q, a in zip(questions, answers):
        if a == q["answer"]:
            correct += 1
        elif q["topic"] not in weak:
            weak.append(q["topic"])
    return correct, weak
