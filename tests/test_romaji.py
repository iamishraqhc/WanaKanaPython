import pytest

from wanakana.romaji import is_romaji, is_char_romaji


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("A", True),
        ("xYz", True),
        ("Tōkyō and Ōsaka", True),
        ("Tokyo and Osaka", True),
        ("あアA", False),
        ("お願い", False),
        ("熟成", False),
        ("a*b&c-d", True),  # Passes Latin punctuation
        ("0123456789", True),  # Passes Latin numbers
        ("a！b&cーd", False),  # Fails Zenkaku punctuation
        ("ｈｅｌｌｏ", False),  # Fails Zenkaku Latin
    ],
)
def test_is_romaji(test_input, expected):
    assert is_romaji(test_input) == expected


@pytest.mark.parametrize(
    "test_input,regex,expected",
    [
        ("a！b&cーd", "[！ー]", True),
        ("a！b&cーd", "[?]", False)
    ],
)
def test_is_japanese_with_regex(test_input, regex, expected):
    assert is_romaji(test_input, regex) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("n", True),
        ("!", True),
        ("ナ", False),
        ("は", False),
        ("缶", False),
    ],
)
def test_is_char_romaji(test_input, expected):
    assert is_char_romaji(test_input) == expected
