def test_single_one_word_anagram(anagrammer):
    available_words = ['secured', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert anagrams == expected_anagrams


def test_multiple_one_word_anagrams(anagrammer):
    available_words = ['secured', 'curesed', 'garbage']
    anagramee = 'rescued'
    expected_anagrams = ['secured', 'curesed']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_two_word_anagram(anagrammer):
    available_words = ['moon', 'starer', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer', 'starer moon']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_unapplicable_sub_matches(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = ['moon starer', 'starer moon']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_applicable_sub_matches(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    expected_anagrams = [
        'moon starer',
        'moron stare',
        'stare moron',
        'starer moon'
    ]

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_minimum_word_length(anagrammer):
    available_words = ['moon', 'starer', 'stare', 'moron', 'garbage']
    anagramee = 'astronomer'
    minimum_word_length = 5
    expected_anagrams = [
        'moron stare',
        'stare moron'
    ]

    anagrams = anagrammer(available_words, minimum_word_length).find_all(anagramee)

    assert sorted(anagrams) == sorted(expected_anagrams)


def test_four_word_anagram_with_spaces_in_input(anagrammer):
    available_words = ['he', 'has', 'that', 'geometry', 'proof', 'garbage', 'red', 'herring']
    anagramee = 'the theorem of pythagoras'
    expected_anagram = 'he has that geometry proof'

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert expected_anagram in anagrams
    assert len(anagrams) == 120


def test_messy_input_with_capital_letters(anagrammer):
    available_words = ['secured', 'garbage']
    anagramee = 'Res Cued!'
    expected_anagrams = ['secured']

    anagrams = anagrammer(available_words).find_all(anagramee)

    assert anagrams == expected_anagrams
