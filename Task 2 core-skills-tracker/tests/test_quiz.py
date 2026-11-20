import unittest

from skilltracker import quiz

QUESTIONS = [
    {"topic": "A", "question": "q1", "options": ["x", "y"], "answer": 0},
    {"topic": "B", "question": "q2", "options": ["x", "y"], "answer": 1},
]


class QuizTests(unittest.TestCase):
    def test_all_correct(self):
        self.assertEqual(quiz.score(QUESTIONS, [0, 1]), (2, []))

    def test_weak_topics(self):
        self.assertEqual(quiz.score(QUESTIONS, [1, 1]), (1, ["A"]))

    def test_wrong_answer_count(self):
        with self.assertRaises(ValueError):
            quiz.score(QUESTIONS, [0])


if __name__ == "__main__":
    unittest.main()
