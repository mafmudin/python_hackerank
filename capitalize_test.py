import unittest
import capitalize


class Test(unittest.TestCase):

    def test_lower(self):
        self.assertEqual(capitalize.solve_with_re("udin sedunia"), "Udin Sedunia")

    def test_uppercase(self):
        self.assertEqual(capitalize.solve_with_re("UDIN SEDUNIA"), "Udin Sedunia")

    def test_start_with_number(self):
        self.assertEqual(capitalize.solve_with_re("123udin Sedunia"), "123udin Sedunia")

    def test_contain_number(self):
        self.assertEqual(capitalize.solve_with_re("udin123 sedunia"), "Udin123 Sedunia")

    def test_single_character(self):
        self.assertEqual(capitalize.solve_with_re("1 w 2 r 3g"), "1 W 2 R 3g")

    def test_single_character2(self):
        self.assertEqual(capitalize.solve_with_re("132 456 Wq  m e"), "132 456 Wq  M E")
