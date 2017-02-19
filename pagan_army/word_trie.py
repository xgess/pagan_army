from collections import UserDict
import os


class _WordTrieNode(UserDict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_a_word = False
        self.depth = 0


class WordTrie(UserDict):

    PATH_TO_DEFAULT_INGESTABLE_WORDS = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'fiftyeightkwords.txt'
    )

    def __init__(self):
        self.data = _WordTrieNode()

    @property
    def root_node(self):
        return self.data

    def add_word(self, word):
        current_node = self.data
        for i in range(len(word)):
            current_letter = word[i]
            current_node[current_letter] = current_node.get(current_letter, _WordTrieNode())
            current_node = current_node[current_letter]
            current_node.depth = i + 1
        current_node.is_a_word = True

    @classmethod
    def from_words(cls, words):
        instance = cls()
        [instance.add_word(word) for word in words]
        return instance

    @classmethod
    def from_file_of_words(cls, path):
        instance = cls()
        with open(path, 'r') as file_handler:
            for line in file_handler:
                instance.add_word(line.rstrip())
        return instance
