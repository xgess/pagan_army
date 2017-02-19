import pytest

from pagan_army.anagram_handler import AnagramHandler


@pytest.fixture
def simple_anagram_generator():
    class SimpleAnagramGenerator:
        def find(self, _):
            return iter(['cat', 'hat', 'bat', 'tab'])
    return SimpleAnagramGenerator()


@pytest.fixture
def duplicates_anagram_generator():
    class DuplicatesAnagramGenerator:
        def find(self, _):
            return iter(['cat hat', 'hat cat', 'chat at', 'at chat'])
    return DuplicatesAnagramGenerator()


def test_it_behaves_like_an_iterator(simple_anagram_generator):
    anagramee = 'whatever'
    anagram_handler = AnagramHandler(anagramee, simple_anagram_generator)
    expected_anagrams = ['cat', 'hat', 'bat', 'tab']

    all_anagrams = [a for a in anagram_handler]

    assert sorted(all_anagrams) == sorted(expected_anagrams)


def test_it_deduplicates_on_the_way_out(duplicates_anagram_generator):
    anagramee = 'whatever'
    anagram_handler = AnagramHandler(anagramee, duplicates_anagram_generator)
    expected_anagrams = ['cat hat', 'at chat']

    all_anagrams = [a for a in anagram_handler]

    assert sorted(all_anagrams) == sorted(expected_anagrams)


def test_get_n(simple_anagram_generator):
    anagramee = 'whatever'
    anagram_handler = AnagramHandler(anagramee, simple_anagram_generator)
    expected_anagrams = ['cat', 'hat', 'bat']

    all_anagrams = anagram_handler.get_n(3)

    assert sorted(all_anagrams) == sorted(expected_anagrams)
