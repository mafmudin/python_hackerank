import unittest
import mutate_string


class MutateStringTest(unittest.TestCase):
    def test_simple_text(self):
        self.assertEqual(mutate_string.mutate_string("udin", 2, "o"), "udon")
