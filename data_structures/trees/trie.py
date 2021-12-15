from collections import deque


class Node:
    def __init__(self, character, parent):
        self.character = character
        if self.character is not None:
            self.character = self.character.lower()
        self.parent = parent
        self.children = dict()
        self.terminus = False

    def add(self, child_node):
        self.children[child_node.character] = child_node


class Trie:

    def __init__(self):
        self._root = Node(None, None)

    # def insert(self, word):
    #     if not word:
    #         return
    #     current_node = self._root
    #     for character in self._normalize_word(word):
    #         if character in current_node.children:
    #             current_node = current_node.children[character]
    #         else:
    #             child_node = Node(character, current_node)
    #             current_node.add(child_node)
    #             current_node = child_node
    #     current_node.terminus = True

    def insert(self, word):
        if not word:
            return
        leaf_node = self._insert(self._normalize_word(word), self._root)
        leaf_node.terminus = True

    def _insert(self, word, node):
        if not word:
            return node
        elif word[0] in node.children:
            return self._insert(word[1:], node.children[word[0]])
        new_node = Node(word[0], node)
        node.add(new_node)
        return self._insert(word[1:], new_node)

    # def __contains__(self, item):
    #     current_node = self._root
    #     for symbol in self._normalize_word(item):
    #         if symbol not in current_node.children:
    #             return False
    #         current_node = current_node.children[symbol]
    #     return current_node.terminus

    def _contains(self, word, node):
        if not word:
            return node.terminus
        return self._contains(word[1:], node.children[word[0]]) if word[0] in node.children else False

    def __contains__(self, item):
        return self._contains(self._normalize_word(item), self._root)

    def _normalize_word(self, word):
        return word.strip().lower()

    def _get_all_words(self, prefix, node, word_list):
        if node.character:
            prefix.append(node.character)
        for child in node.children.values():
            self._get_all_words(prefix, child, word_list)
        if node.terminus:
            word_list.append("".join([i[0] for i in prefix]))
        if len(prefix) > 0:
            prefix.pop()

    def get_possible_words(self, prefix):
        current_node = self._root
        found_prefix = True
        word_list = []
        prefix_deque = deque()
        for symbol in self._normalize_word(prefix):
            if symbol in current_node.children:
                current_node = current_node.children[symbol]
            else:
                found_prefix = False
                break
        if found_prefix:
            self._get_all_words(prefix_deque, current_node, word_list)
            # This is a bit kludgy - add the prefix to the rest of the characters found,
            # but I take off the last character from the prefix because it was added
            # in the _get_all_words method call since it is the current_node being passed into it.
            word_list = list(map(lambda word: prefix[:len(prefix)-1] + word, word_list))

        return word_list

    def get_all_words(self):
        word_list = []
        self._get_all_words(deque(), self._root, word_list)
        return word_list





