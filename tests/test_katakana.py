import pytest

from wanakana.katakana import is_katakana, any_katakana, is_char_katakana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("アア", True),
        ("ア", True),
        ("あ", False),
        ("A", False),
        ("あア", False),
        ("ゲーム", True),
        ("げーむ", False),
        ("痛み", False),
    ],
)
def test_is_katakana(test_input, expected):
    assert is_katakana(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("アア", True),
        ("ア", True),
        ("あ", False),
        ("A", False),
        ("あア", True),
        ("ゲーム", True),
        ("げーむ", True),  # Long dash counts as Hiragana and Katakana
        ("痛み", False),
    ],
)
def test_any_katakana(test_input, expected):
    assert any_katakana(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("ナ", True),
        ("は", False),
        ("n", False),
        ("!", False),
    ],
)
def test_is_char_katakana(test_input, expected):
    assert is_char_katakana(test_input) == expected
