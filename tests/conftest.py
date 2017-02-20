import pytest

from pagan_army.unsorted_trie_anagram_generator import UnsortedTrieAnagramGenerator
from pagan_army.word_trie import WordTrie


@pytest.fixture
def unsorted_trie_anagrammer():
    def inner(available_words, minimum_word_length=2):
        return UnsortedTrieAnagramGenerator(WordTrie.from_words(available_words), minimum_word_length)
    return inner


@pytest.fixture(params=['unsorted_trie_anagrammer'])
def anagrammer(request, unsorted_trie_anagrammer):
    anagrammer_lookup = {
        'unsorted_trie_anagrammer': unsorted_trie_anagrammer
    }
    return anagrammer_lookup[request.param]
