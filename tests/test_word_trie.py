import os

from pagan_army.word_trie import WordTrie


def test_from_words():
    words = ['one', 'onesie', 'two']
    expected_trie_as_dict = {'o': {'n': {'e': {'s': {'i': {'e': {}}}}}}, 't': {'w': {'o': {}}}}

    word_trie = WordTrie.from_words(words)

    assert word_trie == expected_trie_as_dict


def test_from_file(tmpdir):
    words = ['one', 'onesie', 'two']
    temp_file = tmpdir.join("words.txt")
    temp_file.write('\n'.join(words))
    expected_trie_as_dict = {'o': {'n': {'e': {'s': {'i': {'e': {}}}}}}, 't': {'w': {'o': {}}}}

    word_trie = WordTrie.from_file_of_words(temp_file.strpath)

    assert word_trie == expected_trie_as_dict


def test_default_dictionary_path_exists():
    is_dictionary_there = os.path.isfile(WordTrie.PATH_TO_DEFAULT_INGESTABLE_WORDS)

    assert is_dictionary_there == True
