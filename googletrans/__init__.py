import re
import html
import urllib.request
import urllib.parse

__version__ = "0.2.0"

def translate(to_translate: str, to_language: str = "auto", from_language: str = "auto") -> str:
    """
    Translates a text from one language to another using the Google Translate API.

    Args:
        to_translate (str): The text to translate.
        to_language (str, optional): The language to translate the text to. Defaults to "auto".
        from_language (str, optional): The language of the text to translate. Defaults to "auto".

    Returns:
        str: The translated text.
    """
    link = f"http://translate.google.com/m?tl={to_language}&sl={from_language}&q={urllib.parse.quote(to_translate)}"
    request = urllib.request.Request(link, headers={
        'User-Agent': "Mozilla/4.0 (compatible;MSIE 6.0;Windows NT 5.1;SV1;.NET CLR 1.1.4322;.NET CLR 2.0.50727;.NET CLR 3.0.04506.30)"})
    re_result = re.findall(
        r'(?s)class="(?:t0|result-container)">(.*?)<', urllib.request.urlopen(request).read().decode("utf-8"))
    return "" if len(re_result) == 0 else html.unescape(re_result[0])


if __name__ == "__main__":
    print(translate("Hello, my name is Python.", "ko"))

