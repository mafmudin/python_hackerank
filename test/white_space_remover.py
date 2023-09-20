import unittest

import remove_witespace


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_witespace.remove_white_space("Mafm udin"), "Mafmudin")

    def test_complex(self):
        self.assertEqual(remove_witespace.remove_white_space("Muchamad $mafmudin 123 udin&\n\r\t nama udin"), "Muchamad$mafmudin123udin&namaudin")  # add assertion here


if __name__ == '__main__':
    unittest.main()
