import pytest

from wanakana.kana import is_kana, any_kana


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("あ", True),
        ("ア", True),
        ("あア", True),
        ("A", False),
        ("あAア", False),
        ("げーむ", True),  # Ignores long dash in mixed Kana
        ("痛み", False),
        ("アーあ", True),
    ],
)
def test_is_kana(test_input, expected):
    assert is_kana(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("あ", True),
        ("ア", True),
        ("あア", True),
        ("A", False),
        ("あAア", True),
        ("げーむ", True),  # Ignores long dash in mixed Kana
        ("痛み", True),
        ("アーあ", True),
    ],
)
def test_any_kana(test_input, expected):
    assert any_kana(test_input) == expected
