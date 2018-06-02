<div align="center">
<h1>WanaKanaPython</h1>
<h4>A Python library to assist in detecting Japanese text</h4>
</div>

## Usage

### Install

```shell
pip install wanakana
```

```python
from wanakana import hiragana
hiragana.is_hiragana("げーむ")

or

from wanakana.hiragana import is_hiragana
is_hiragana("げーむ")
```

## Documentation

See original [WanaKana docs](http://wanakana.com/docs/global.html) as the functions are near identical.

## Quick Reference

```python
is_japanese("泣き虫。！〜２￥ｚｅｎｋａｋｕ")
// => true

is_kana("あーア")
// => true

is_hiragana("げーむ")
// => true

is_katakana("ゲーム")
// => true

is_kanji("切腹")
// => true

is_romaji("Tōkyō and Ōsaka")
// => true
```

## Credits

A partial port of [WanaKana](https://github.com/wanikani/wanakana)

## License

Source files of this project are available under the MIT License. See [LICENSE](LICENSE)