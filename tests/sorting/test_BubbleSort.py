import unittest
from algorithms.sorting.BubbleSort import something


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4, something())  # add assertion here


if __name__ == '__main__':
    unittest.main()
