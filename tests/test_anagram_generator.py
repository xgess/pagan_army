from pagan_army.basic_anagram_generator import BasicAnagramGenerator


def test_single_one_word_anagram(build_basic_trie):
    available_words = ['secured', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured']

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert anagrams == expected_anagrams


def test_multiple_one_word_anagrams(build_basic_trie):
    available_words = ['secured', 'curesed', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured', 'curesed']

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_two_word_anagram(build_basic_trie):
    available_words = ['moon', 'starer', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer', 'starer moon']

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_unapplicable_sub_matches(build_basic_trie):
    available_words = ['moon', 'starer', 'stare', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer', 'starer moon']

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_applicable_sub_matches(build_basic_trie):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = [
        'moon starer',
        'moron stare',
        'stare moron',
        'starer moon'
    ]

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_minimum_word_length(build_basic_trie):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    minimum_word_length = 5
    expected_anagrams = [
        'moron stare',
        'stare moron'
    ]

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words), minimum_word_length).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_four_word_anagram_with_spaces_in_input(build_basic_trie):
    available_words = ['he', 'has', 'that', 'geometry', 'proof', 'garbage', 'red', 'herring']
    anagramee = 'the theorem of pythagoras'
    minimum_word_length = 2
    expected_anagram = 'he has that geometry proof'

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words), minimum_word_length).find_all(anagramee)

    assert expected_anagram in anagrams
    assert len(anagrams) == 120


def test_messy_input_with_capital_letters(build_basic_trie):
    available_words = ['secured', 'garbage']
    anagramee = 'Res Cued!'
    expected_anagrams = ['secured']

    anagrams = BasicAnagramGenerator(build_basic_trie(available_words)).find_all(anagramee)

    assert anagrams == expected_anagrams
