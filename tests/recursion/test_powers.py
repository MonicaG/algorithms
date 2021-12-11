import unittest
from algorithms.recursion import powers


class TestPowers(unittest.TestCase):

    def test(self):
        assert powers.recursive_power(5, 0) == 1
        assert powers.recursive_power(5, 1) == 5
        assert powers.recursive_power(5, 2) == 25
