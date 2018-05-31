import pytest

from wanakana.hiragana import is_hiragana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("あ", True),
        ("ああ", True),
        ("ア", False),
        ("A", False),
        ("あア", False),
        ("げーむ", True),  # Ignores long dash in Hiragana
    ],
)
def test_is_hiragana(test_input, expected):
    assert is_hiragana(test_input) == expected
