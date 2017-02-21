import itertools

from pagan_army.word_hash import WordHash


class HashAnagramGenerator:

    LETTERS_TO_IGNORE_FROM_INPUT = list(' ,.-:!?;"\'')

    def __init__(self, word_data_structure=None, minimum_word_length=3):
        self.minimum_word_length = minimum_word_length
        if not word_data_structure:
            word_data_structure = WordHash.from_file_of_words(WordHash.PATH_TO_DEFAULT_INGESTABLE_WORDS)
        self.word_hash = word_data_structure

    def find_all(self, anagramee):
        return [a for a in self.find(anagramee)]

    def find(self, anagramee):
        cleaned_input = ''
        for letter in anagramee.lower():
            if letter in self.LETTERS_TO_IGNORE_FROM_INPUT:
                continue
            cleaned_input = cleaned_input + letter

        def inner(available_letters, buildup):
            if not available_letters:
                # exit condition
                yield buildup
            elif len(available_letters) < self.minimum_word_length:
                pass
            elif self.word_hash.exact_matches(available_letters):
                for match in self.word_hash.exact_matches(available_letters):
                    yield from inner([], ' '.join([buildup, match]).strip())

            half_of_remaining_letters = len(available_letters) // 2

            list_of_combos = []
            for number_of_letters in range(self.minimum_word_length, half_of_remaining_letters+1):
                list_of_combos.append(itertools.combinations(available_letters, number_of_letters))
            all_available_combos = itertools.chain(*list_of_combos)

            for combo in all_available_combos:
                for match in self.word_hash.exact_matches(''.join(combo)):
                    remaining_letters = list(available_letters)
                    [remaining_letters.remove(letter) for letter in combo]
                    yield from inner(remaining_letters, ' '.join([buildup, match]).strip())

        yield from inner(list(cleaned_input), '')
