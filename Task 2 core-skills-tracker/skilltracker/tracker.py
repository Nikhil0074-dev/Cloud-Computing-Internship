"""Core logic: concepts, practice, mini projects and mentor feedback."""
from datetime import date


def _find_concept(data, name):
    for concept in data["concepts"]:
        if concept["name"].lower() == name.lower():
            return concept
    return None


def add_concept(data, name, why):
    """Add a concept with the reason it matters (the 'why')."""
    name = name.strip()
    why = why.strip()
    if not name or not why:
        raise ValueError("Name and reason are both required.")
    if _find_concept(data, name):
        raise ValueError(f"Concept '{name}' already exists.")
    data["concepts"].append({"name": name, "why": why, "done": False})


def log_practice(data, concept, note, minutes):
    """Record one practice session for a concept."""
    matched_concept = _find_concept(data, concept)
    if not matched_concept:
        raise ValueError(f"Concept '{concept}' not found. Add it first.")
    note = note.strip()
    if not note:
        raise ValueError("Practice note cannot be empty.")
    if minutes <= 0:
        raise ValueError("Minutes must be more than zero.")
    data["practice"].append(
        {"concept": matched_concept["name"], "note": note, "minutes": minutes, "date": str(date.today())}
    )


def add_project(data, name, concept):
    """Record a small project that proves one concept."""
    name = name.strip()
    matched_concept = _find_concept(data, concept)
    if not name:
        raise ValueError("Project name cannot be empty.")
    if not matched_concept:
        raise ValueError(f"Concept '{concept}' not found. Add it first.")
    data["projects"].append({"name": name, "concept": matched_concept["name"]})
    matched_concept["done"] = True


def add_feedback(data, text):
    """Record mentor feedback. It starts as not fixed."""
    if not text.strip():
        raise ValueError("Feedback cannot be empty.")
    data["feedback"].append({"text": text.strip(), "fixed": False, "date": str(date.today())})


def mark_feedback_fixed(data, index):
    """Mark a feedback item (1, 2, 3...) as fixed."""
    if index < 1 or index > len(data["feedback"]):
        raise ValueError("No feedback with that number.")
    data["feedback"][index - 1]["fixed"] = True


def summary(data):
    """Return key numbers about progress."""
    total = len(data["concepts"])
    done = sum(1 for c in data["concepts"] if c["done"])
    open_feedback = sum(1 for f in data["feedback"] if not f["fixed"])
    return {
        "concepts": total,
        "concepts_with_project": done,
        "practice_minutes": sum(p["minutes"] for p in data["practice"]),
        "projects": len(data["projects"]),
        "open_feedback": open_feedback,
        "percent_done": round(100 * done / total) if total else 0,
    }
