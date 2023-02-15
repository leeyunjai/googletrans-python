# Google Translate API for Python

This is a Python library that provides an interface to the Google Translate API.

## Installation

You can install this library using pip:

```bash
pip3 install googletrans-python
```

## Usage

```python
import googletrans as gt

# Translate text from English to Korean
print(gt.translate("Hello, How are you?", "ko"))

# Translate text from English to Japanese
print(gt.translate("Hello, How are you?", "ja"))

# Translate text from English to French
print(gt.translate("Hello, How are you?", "fr"))
```

```bash
안녕하세요. 어떻게 지내세요?
こんにちは元気ですか？
Bonjour comment allez-vous?
```
unofficial
