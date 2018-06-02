import pytest

from wanakana.japanese import is_japanese, is_char_japanese


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("泣き虫", True),
        ("あア", True),
        ("２月", True),  # Zenkaku numbers allowed
        ("泣き虫。！〜＄", True),  # Zenkaku/JA punctuation
        ("泣き虫.!~$", False),  # Latin punctuation fails
        ("A泣き虫", False),
        ("≪偽括弧≫", False),
        ("A", False),
        ("泣き虫。＃！〜〈〉《》〔〕［］【】（）｛｝〝〟", True),  # With Zenkaku punctuation
        ("泣き虫.!~", False),  # Romaji punctuation is not Japanese
        ("０１２３４５６７８９", True),  # Zenkaku numbers are Japanese
        ("0123456789", False),  # Latin numbers are not Japanese
        ("　", True),  # Japanese space is Japanese
        (" ", False),  # English space is not Japanese
        ("ＭｅＴｏｏ", True),  # Zenkaku latin letters are Japanese
        ("２０１１年", True),  # Mixed with numbers is Japanese
        ("ﾊﾝｶｸｶﾀｶﾅ", True),  # Hankaku Katakana is Japanese
        ("Latin text", False),
    ],
)
def test_is_japanese(test_input, expected):
    assert is_japanese(test_input) == expected


@pytest.mark.parametrize(
    "test_input,regex,expected",
    [
        ("≪偽括弧≫", "[≪≫]", True),
        ("≪偽括弧≫", "[a]", False)
    ],
)
def test_is_japanese_with_regex(test_input, regex, expected):
    assert is_japanese(test_input, regex) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("１", True),
        ("ナ", True),
        ("は", True),
        ("缶", True),
        ("〜", True),
        ("ｎ", True),
        ("Ｋ", True),
        ("1", False),
        ("n", False),
        ("K", False),
        ("!", False),
    ],
)
def test_is_char_japanese(test_input, expected):
    assert is_char_japanese(test_input) == expected
