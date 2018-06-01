import pytest

from wanakana.constants import HIRAGANA_START, HIRAGANA_END
from wanakana.utils import is_char_in_range, is_char_long_dash


@pytest.mark.parametrize(
    "test_input,start,end,expected",
    [
        ("", None, None, False),
        (None, None, None, False),
        ("は", HIRAGANA_START, HIRAGANA_END, True),
        ("d", HIRAGANA_START, HIRAGANA_END, False),
    ],
)
def test_is_char_in_range(test_input, start, end, expected):
    assert is_char_in_range(test_input, start, end) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", False),
        (None, False),
        ("ー", True),
        ("-", False),
        ("f", False),
        ("ふ", False),
    ],
)
def test_is_char_long_dash(test_input, expected):
    assert is_char_long_dash(test_input) == expected
