import pytest

from wanakana.romaji import is_romaji


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
