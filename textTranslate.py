# 文本翻译功能
from googletrans import Translator


# 初始化文本
translator = Translator()


# 文本翻译
def translatorText(text: str, src: str, dest: str):
    translated = translator.translate(text, src=src, dest=dest)
    return translated.text
