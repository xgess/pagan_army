def collapse_and_sort(anagrams):
    good_anagrams = set()
    for anagram in anagrams:
        words = anagram.split(' ')
        sorted_words = ' '.join(sorted(words))
        good_anagrams.add(sorted_words)
    return good_anagrams


def test_single_one_word_anagram(anagrammer):
    available_words = ['secured', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_multiple_one_word_anagrams(anagrammer):
    available_words = ['secured', 'curesed', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured', 'curesed']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_two_word_anagram(anagrammer):
    available_words = ['moon', 'starer', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_unapplicable_sub_matches(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_applicable_sub_matches(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    minimum_word_length = 3
    expected_anagrams = ['moon starer', 'moron stare']

    anagrams = anagrammer(available_words, minimum_word_length).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_minimum_word_length(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    minimum_word_length = 5
    expected_anagrams = ['stare moron']

    anagrams = anagrammer(available_words, minimum_word_length).find_all(anagramee)

    assert collapse_and_sort(anagrams) == collapse_and_sort(expected_anagrams)


def test_four_word_anagram_with_spaces_in_input(anagrammer):
    available_words = ['built', 'to', 'stay', 'free', 'garbage', 'red', 'herring']
    anagramee = 'statue of liberty'
    expected_anagrams = ['built to stay free']

    anagrams = anagrammer(available_words, minimum_word_length=2).find_all(anagramee)

    assert collapse_and_sort(expected_anagrams) == collapse_and_sort(anagrams)


def test_anagram_with_large_word(anagrammer):
    available_words = ['naughtiness', 'drug', 'garbage']
    anagramee = 'guinness draught'
    expected_anagrams = ['naughtiness drug']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(expected_anagrams) == collapse_and_sort(anagrams)


def test_messy_input_with_capital_letters(anagrammer):
    available_words = ['secured', 'garbage']
    anagramee = 'Res Cued!'
    expected_anagrams = ['secured']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert collapse_and_sort(expected_anagrams) == collapse_and_sort(anagrams)
