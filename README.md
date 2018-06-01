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
```

## Documentation

See the docs folder

## Quick Reference

```python
wanakana.isJapanese('泣き虫。！〜２￥ｚｅｎｋａｋｕ')
// => true

wanakana.isKana('あーア')
// => true

wanakana.isHiragana('げーむ')
// => true

wanakana.isKatakana('ゲーム')
// => true

wanakana.isKanji('切腹')
// => true

wanakana.isRomaji('Tōkyō and Ōsaka')
// => true
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md)

## Credits

A partial port of [WanaKana](https://github.com/wanikani/wanakana)

## License

Source files of this project are available under MIT License. See [LICENSE](LICENSE)