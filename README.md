# 🌍 googletrans-python

<p align="center">
  <img src="https://img.shields.io/pypi/v/googletrans-python?style=for-the-badge&color=blue" />
  <img src="https://img.shields.io/pypi/pyversions/googletrans-python?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/leeyunjai/googletrans-python?style=for-the-badge" />
  <img src="https://img.shields.io/pypi/l/googletrans-python?style=for-the-badge&color=green" />
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <b>Google Translate in one line of Python. No API key. No dependencies. Just works.</b>
</p>

---

## Why This Exists

Every other Google Translate library is either **broken**, **bloated**, or **requires an API key**.

This one doesn't.

```python
import googletrans as gt

gt.translate("Hello, World!", "ko")
# → '안녕하세요, 월드!'
```

That's it. No setup, no tokens, no `httpx`, no `requests`. Just the standard library.

## Installation

```bash
pip install googletrans-python
```

## Usage

```python
import googletrans as gt

# English → Korean
gt.translate("Good morning", "ko")
# → '좋은 아침'

# English → Japanese
gt.translate("Good morning", "ja")
# → 'おはようございます'

# English → French
gt.translate("Good morning", "fr")
# → 'Bonjour'

# Auto-detect source language
gt.translate("Bonjour le monde", "en")
# → 'Hello world'

# Specify source language explicitly
gt.translate("こんにちは", "en", from_language="ja")
# → 'Hello'
```

### API

```python
googletrans.translate(
    to_translate: str,           # Text to translate
    to_language: str,            # Target language code
    from_language: str = "auto"  # Source language (auto-detected by default)
) -> str
```

### Supported Languages

All [Google Translate language codes](https://cloud.google.com/translate/docs/languages) are supported. Common ones:

| Code | Language | Code | Language | Code | Language |
|------|----------|------|----------|------|----------|
| `en` | English | `ko` | Korean | `ja` | Japanese |
| `zh-CN` | Chinese (Simplified) | `zh-TW` | Chinese (Traditional) | `fr` | French |
| `de` | German | `es` | Spanish | `pt` | Portuguese |
| `ru` | Russian | `ar` | Arabic | `hi` | Hindi |
| `vi` | Vietnamese | `th` | Thai | `id` | Indonesian |

## How It Works

No REST API. No OAuth. No client library.

It hits Google Translate's **mobile web endpoint** (`translate.google.com/m`) and parses the result — the same page your browser renders when you visit Google Translate on a phone.

```
urllib.request → translate.google.com/m → regex parse → translated text
```

The entire implementation is **one function, ~15 lines of code**, with zero external dependencies.

## Comparison

| Library | API Key | Dependencies | Working (2025) |
|---------|---------|-------------|----------------|
| **googletrans-python** | ❌ Not needed | **0** | ✅ |
| googletrans 4.0.0-rc1 | ❌ | httpx | ⚠️ Frequently broken |
| google-cloud-translate | ✅ Required | grpcio, google-auth, ... | ✅ (paid) |
| deep-translator | ❌ | requests, beautifulsoup4 | ⚠️ Rate-limited |

## Limitations

Be aware of these tradeoffs — this is a scraping-based approach, not an official API:

- **Rate limiting** — Google may throttle or block IPs making too many requests
- **No batch translation** — One call per string
- **No detection API** — Can't return detected language metadata (auto-detect still works for translation)
- **Unofficial** — Google can change the page structure at any time

For production workloads with high volume, consider the [official Cloud Translation API](https://cloud.google.com/translate).

## License

MIT

---

<p align="center">
  <sub>If this saved you from setting up a GCP project just to translate one string, consider leaving a ⭐</sub>
</p>
