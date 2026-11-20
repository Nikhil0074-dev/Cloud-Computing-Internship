import unittest

from skilltracker import tracker


def fresh():
    return {"concepts": [], "practice": [], "projects": [], "feedback": []}


class TrackerTests(unittest.TestCase):
    def test_add_concept(self):
        d = fresh()
        tracker.add_concept(d, "Testing", "Finds errors early")
        self.assertEqual(len(d["concepts"]), 1)

    def test_duplicate_concept_rejected(self):
        d = fresh()
        tracker.add_concept(d, "Testing", "why")
        with self.assertRaises(ValueError):
            tracker.add_concept(d, "testing", "why")

    def test_duplicate_concept_rejected_after_trimming(self):
        d = fresh()
        tracker.add_concept(d, "Testing", "why")
        with self.assertRaises(ValueError):
            tracker.add_concept(d, " testing ", "another reason")

    def test_empty_values_rejected(self):
        with self.assertRaises(ValueError):
            tracker.add_concept(fresh(), "", "why")

    def test_practice_needs_known_concept(self):
        with self.assertRaises(ValueError):
            tracker.log_practice(fresh(), "Nope", "note", 10)

    def test_practice_minutes_must_be_positive(self):
        d = fresh()
        tracker.add_concept(d, "A", "why")
        with self.assertRaises(ValueError):
            tracker.log_practice(d, "A", "note", 0)

    def test_practice_note_must_not_be_empty(self):
        d = fresh()
        tracker.add_concept(d, "A", "why")
        with self.assertRaises(ValueError):
            tracker.log_practice(d, "A", "   ", 10)

    def test_project_name_must_not_be_empty(self):
        d = fresh()
        tracker.add_concept(d, "A", "why")
        with self.assertRaises(ValueError):
            tracker.add_project(d, "   ", "A")

    def test_project_marks_concept_done(self):
        d = fresh()
        tracker.add_concept(d, "A", "why")
        tracker.add_project(d, "Proj", "A")
        self.assertTrue(d["concepts"][0]["done"])

    def test_feedback_flow(self):
        d = fresh()
        tracker.add_feedback(d, "Write more tests")
        self.assertEqual(tracker.summary(d)["open_feedback"], 1)
        tracker.mark_feedback_fixed(d, 1)
        self.assertEqual(tracker.summary(d)["open_feedback"], 0)

    def test_bad_feedback_number(self):
        with self.assertRaises(ValueError):
            tracker.mark_feedback_fixed(fresh(), 1)

    def test_summary_percent(self):
        d = fresh()
        tracker.add_concept(d, "A", "why")
        tracker.add_concept(d, "B", "why")
        tracker.add_project(d, "P", "A")
        self.assertEqual(tracker.summary(d)["percent_done"], 50)

    def test_summary_empty(self):
        self.assertEqual(tracker.summary(fresh())["percent_done"], 0)


if __name__ == "__main__":
    unittest.main()
