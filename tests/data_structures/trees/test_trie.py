import unittest
from data_structures.trees import trie


class TestTrie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #            root
        #          /      \
        #       /           \
        #     a *             b
        #    / \             /
        #   d   n *         a
        #  /   / \       /  |  \
        # d * d * y *   g * t *  y *
        #              / \   \
        #             e   s * h *
        #            /
        #           l *
        # asterisk denotes a word

        cls._trie = trie.Trie()
        cls._trie.insert("a")
        cls._trie.insert("add")
        cls._trie.insert("an")
        cls._trie.insert("and")
        cls._trie.insert("any")
        cls._trie.insert("bagel")
        cls._trie.insert("bag")
        cls._trie.insert("bags")
        cls._trie.insert("bat")
        cls._trie.insert("bath")
        cls._trie.insert("bay")

        cls._trie_length = 11 # magic number, the number of words in the trie

    def test(self):
        assert len(self._trie.get_all_words()) == self._trie_length

        assert "a" in self._trie
        assert "add" in self._trie
        assert "an" in self._trie
        assert "and" in self._trie
        assert "any" in self._trie
        assert "bagel" in self._trie
        assert "bag" in self._trie
        assert "bags" in self._trie
        assert "bat" in self._trie
        assert "bath" in self._trie
        assert "bay" in self._trie

    def test_duplicate_entries(self):
        """Adding a word that already exists should not create a new word in the trie"""
        t = self._trie
        t.insert("bag")

        assert len(t.get_all_words()) == self._trie_length
        assert "bag" in t

    def test_mixed_case(self):
        """insert and retrieval are case insensitive"""
        t = trie.Trie()
        t.insert("APPLE")
        t.insert("oRANge")

        assert "apple" in t
        assert "orange" in t

        assert "APPLE" in t
        assert "ORANGE" in t

        assert "aPpLe" in t
        assert "oRangE" in t

    def test_hyphenated_words(self):
        t = trie.Trie()
        t.insert("e-mail")
        t.insert("above-said")
        t.insert("above-water")
        t.insert("above-written")
        t.insert("above")
        t.insert("abode")
        t.insert("exit")

        assert len(t.get_all_words()) == 7

        assert "abode" in t
        assert "above" in t
        assert "above-written" in t
        assert "above-water" in t
        assert "above-said" in t
        assert "e-mail" in t
        assert "exit" in t

    def test_empty_trie(self):
        t = trie.Trie()
        assert len(t.get_all_words()) == 0

    def test_first_symbol_is_a_word(self):
        t = trie.Trie()
        t.insert("a")
        t.insert("apple")

        assert "a" in t
        assert "apple" in t

        words = t.get_all_words()
        assert len(words) == 2
        assert "a" in words
        assert "apple" in words

    def test_get_possible_words(self):
        prefix = 'an'
        expected_words = ['an', 'and', 'any']
        actual_words = self._trie.get_possible_words(prefix)
        assert len(expected_words) == len(actual_words)
        for word in expected_words:
            assert word in actual_words

        prefix = 'ba'
        expected_words = ["bagel", "bag", "bags", "bat", "bath", "bay"]
        actual_words = self._trie.get_possible_words(prefix)
        assert len(expected_words) == len(actual_words)
        for word in expected_words:
            assert word in actual_words

    def test_get_possible_words_no_more_words(self):
        """test that given a prefix that is a terminus with no children in the trie, returns that one word"""
        prefix = 'any'
        actual_words = self._trie.get_possible_words(prefix)
        assert len(actual_words) == 1
        assert prefix in actual_words

    def test_get_possible_words_prefix_not_in_trie(self):
        prefix = 'z'
        actual_words = self._trie.get_possible_words(prefix)
        assert len(actual_words) == 0

    def test_leading_and_trailing_white_space_is_removed(self):
        t = trie.Trie()
        t.insert(" a ")
        t.insert("an")
        t.insert(" and ")

        assert "a" in t
        assert "an" in t
        assert "and" in t

        assert " and " in t

    # def test_dictionary(self):
    #     t = trie.Trie()
    #     with open('/usr/share/dict/words') as f:
    #         for line in f:
    #             t.insert(line)
    #
    #     words = t.get_all_words()
    #     with open('/usr/share/dict/words') as f:
    #         for line in f:
    #             if line not in words:
    #                 print(line)


