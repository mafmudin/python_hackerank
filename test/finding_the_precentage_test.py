import unittest

import finding_the_percentage


class TestFindingThePercentage(unittest.TestCase):
    def test_simple(self):
        student_marks = {}
        name, *line = "udin 1 2 3 4".split()
        scores = list(map(float, line))
        student_marks[name] = scores
        self.assertEqual(finding_the_percentage.finding_the_percentage(student_marks, "udin"), "2.50")

    def test_simple_no_one(self):
        student_marks = {}
        name, *line = "udin 1 2 3 4".split()
        scores = list(map(float, line))
        student_marks[name] = scores
        self.assertEqual(finding_the_percentage.finding_the_percentage(student_marks, "nopal"), "0")
