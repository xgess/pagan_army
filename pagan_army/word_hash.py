import os
from collections import defaultdict


class WordHash:

    PATH_TO_DEFAULT_INGESTABLE_WORDS = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'fiftyeightkwords.txt'
    )

    def __init__(self):
        self.data = defaultdict(set)

    def add_word(self, word):
        sorted_letters = ''.join(sorted(word))
        self.data[sorted_letters].add(word)

    def exact_matches(self, letters):
        if isinstance(letters, list):
            letters = ''.join(letters)
        sorted_letters = ''.join(sorted(letters))
        return self.data[sorted_letters]

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
