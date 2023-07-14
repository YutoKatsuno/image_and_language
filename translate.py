# STEP4 文字を翻訳する
# https://github.com/DeepLcom/deepl-python
import deepl
import os

API_KEY = os.environ["API_KEY"]


def translate(lang: int, txt: str) -> str:
    translator = deepl.Translator(API_KEY)

    if lang == 0:
        # 英語を日本語に翻訳する
        result = translator.translate_text(txt, target_lang="JA")
    else:
        # 日本語を英語に翻訳する
        result = translator.translate_text(txt, target_lang="EN-US")

    return result.text
