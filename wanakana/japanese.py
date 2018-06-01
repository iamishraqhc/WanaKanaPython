from wanakana.constants import JAPANESE_RANGES
from wanakana.utils import is_char_in_range


def is_japanese(text: str) -> bool:
    if not text:
        return False

    return all(is_char_japanese(char) for char in text)


def is_char_japanese(char: str) -> bool:
    if not char:
        return False

    return any(is_char_in_range(char, start, end) for (start, end) in JAPANESE_RANGES)
