# STEP4 文字を翻訳する
# https://github.com/DeepLcom/deepl-python
import deepl
import os

API_KEY = os.environ["API_KEY"]


def translate(txt):
    translator = deepl.Translator(API_KEY)

    text = txt
    en_us = translator.translate_text(f"アメリカ英語: {text}", target_lang="EN-US")
    print(en_us.text)


translate("おはようございます")
