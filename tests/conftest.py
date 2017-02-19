import pytest

from pagan_army.word_trie import WordTrie


@pytest.fixture
def build_basic_trie():
    def build_word_trie(words):
        return WordTrie.from_words(words)
    return build_word_trie
