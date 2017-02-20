from pagan_army.basic_anagram_generator import BasicAnagramGenerator


class AnagramHandler:

    def __init__(self, anagramee, anagram_generator=None, minimum_word_length=3):
        if not anagram_generator:
            anagram_generator = BasicAnagramGenerator(minimum_word_length=minimum_word_length)
        self.all_anagrams = anagram_generator.find(anagramee)
        self.exposable_anagrams = set()

    def __iter__(self):
        return self

    def __next__(self):
        next_anagram = self._get_next_and_standardize()
        while next_anagram in self.exposable_anagrams:
            next_anagram = self._get_next_and_standardize()
        self.exposable_anagrams.add(next_anagram)
        return next_anagram

    def get_n(self, n):
        n_anagrams = []
        try:
            for i in range(n):
                n_anagrams.append(next(self))
        except StopIteration:
            pass
        return n_anagrams

    def _get_next_and_standardize(self):
        # iterate and then sort the string so duplicates can be identified
        # "watchtower along the all" => "all along the watchtower"
        # "along watchtower all the" => "all along the watchtower"
        return ' '.join(sorted(next(self.all_anagrams).split()))
