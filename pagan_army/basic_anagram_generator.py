from pagan_army.word_trie import WordTrie


class BasicAnagramGenerator:

    LETTERS_TO_IGNORE_FROM_INPUT = list(' ,.-:!?;"\'')

    def __init__(self, word_data_structure=None, minimum_word_length=3):
        if not word_data_structure:
            word_data_structure = WordTrie.from_file_of_words(WordTrie.PATH_TO_DEFAULT_INGESTABLE_WORDS)
        self.root_node = word_data_structure.root_node
        self.minimum_word_length = minimum_word_length

    def find_all(self, anagramee):
        return [a for a in self.find(anagramee)]

    def find(self, anagramee):
        def _is_a_complete_anagram(current_trie_node, remaining_letters):
            number_of_available_letters = sum(remaining_letters.values())
            return current_trie_node.is_a_word and \
                number_of_available_letters == 0 and \
                current_trie_node.depth >= self.minimum_word_length

        def _is_a_partial_anagram_word(current_trie_node, remaining_letters):
            number_of_available_letters = sum(remaining_letters.values())
            return current_trie_node.is_a_word and \
                number_of_available_letters > 0 and \
                current_trie_node.depth >= self.minimum_word_length

        def inner(remaining_letters, trie_path, current_trie_node):
            if _is_a_complete_anagram(current_trie_node, remaining_letters):
                completed_anagram = ''.join(trie_path)
                yield completed_anagram
            elif _is_a_partial_anagram_word(current_trie_node, remaining_letters):
                # we have a word but also remaining letters
                # add a space to the path and go back to the root node for a new word
                trie_path.append(' ')
                partially_complete_restart_from_root = inner(
                    remaining_letters=remaining_letters,
                    trie_path=trie_path,
                    current_trie_node=self.root_node
                )
                for word in partially_complete_restart_from_root:
                    # multi-word anagrams here
                    yield word
                # in case another longer word exists, remove the space and keep going
                trie_path.pop()

            for letter, next_node in current_trie_node.items():
                if not remaining_letters.get(letter):
                    # dictionary letter not in available letters
                    continue
                # decrement and append to the trie_path
                remaining_letters[letter] = remaining_letters[letter] - 1
                trie_path.append(letter)
                # recurse to check if this is a complete word
                for word in inner(remaining_letters, trie_path, next_node):
                    yield word
                # remove the added letter from the trie_path and continue
                trie_path.pop()
                remaining_letters[letter] = remaining_letters[letter] + 1

        available_letters = {}
        for letter in anagramee.lower():
            if letter in self.LETTERS_TO_IGNORE_FROM_INPUT:
                continue
            available_letters[letter] = available_letters.get(letter, 0) + 1

        yield from inner(
            remaining_letters=available_letters,
            trie_path=[],
            current_trie_node=self.root_node
        )
