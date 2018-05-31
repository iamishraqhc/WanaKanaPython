import pytest

from wanakana.mixed import is_mixed


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Aア", True),
        ("Aあ", True),
        ("Aあア", True),
        ("２あア", False),
        ("お腹A", True),
        ("お腹", False),
        ("腹", False),
        ("A", False),
        ("あ", False),
        ("ア", False),
    ],
)
def test_is_mixed(test_input, expected):
    assert is_mixed(test_input) == expected


def test_is_mixed_with_pass_kanji_false():
    assert not is_mixed("お腹A", pass_kanji=False)
