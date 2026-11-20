import os
import tempfile
import unittest

from skilltracker import storage


class StorageTests(unittest.TestCase):
    def test_missing_file_gives_empty_data(self):
        data = storage.load("does_not_exist.json")
        self.assertEqual(data["concepts"], [])

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "sub", "p.json")
            data = {"concepts": [{"name": "A"}], "practice": [], "projects": [], "feedback": []}
            storage.save(path, data)
            self.assertEqual(storage.load(path)["concepts"][0]["name"], "A")


if __name__ == "__main__":
    unittest.main()
