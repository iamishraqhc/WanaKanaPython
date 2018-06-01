import pytest

from wanakana.kanji import is_kanji, any_kanji, is_char_kanji


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("切腹", True),
        ("刀", True),
        ("🐸", False),
        ("あ", False),
        ("ア", False),
        ("あア", False),
        ("A", False),
        ("あAア", False),
        ("１２隻", False),
        ("12隻", False),
        ("隻。", False),
    ],
)
def test_is_kanji(test_input, expected):
    assert is_kanji(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("切腹", True),
        ("刀", True),
        ("🐸", False),
        ("あ", False),
        ("ア", False),
        ("あア", False),
        ("A", False),
        ("あAア", False),
        ("１２隻", True),
        ("12隻", True),
        ("隻。", True),
    ],
)
def test_any_kanji(test_input, expected):
    assert any_kanji(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("腹", True),
        ("一", True),  # Kanji for いち・1 - not a long hyphen
        ("ー", False),  # Long hyphen
        ("は", False),
        ("ナ", False),
        ("n", False),
        ("!", False),
    ],
)
def test_is_char_kanji(test_input, expected):
    assert is_char_kanji(test_input) == expected
