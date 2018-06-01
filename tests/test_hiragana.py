import pytest

from wanakana.hiragana import is_hiragana, any_hiragana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("あ", True),
        ("ああ", True),
        ("ア", False),
        ("A", False),
        ("あア", False),
        ("げーむ", True),  # Ignores long dash in Hiragana
        ("痛み", False),
    ],
)
def test_is_hiragana(test_input, expected):
    assert is_hiragana(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("あ", True),
        ("ああ", True),
        ("ア", False),
        ("A", False),
        ("あア", True),
        ("げーむ", True),  # Ignores long dash in Hiragana
        ("痛み", True),
    ],
)
def test_any_hiragana(test_input, expected):
    assert any_hiragana(test_input) == expected
