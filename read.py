# STEP2 画像の文字を取得する

from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    # Tesseractをインストールしてないとここを通る
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use lang '%s'" % tool.get_name())

# 初期では日本語はインストールされていない
# https://github.com/tesseract-ocr/tessdata/raw/4.00/jpn.traineddata
# https://github.com/tesseract-ocr/tessdata_best/blob/main/jpn_vert.traineddata
# これらをダウンロードして、/opt/homebrew/Cellar/tesseract/5.2.0/share/tessdata/に移動させると使えた
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % lang)

img = Image.open("images/sample.jpg")
# 何も表示されていない時はtesseract_layoutの値を調整する
# tesseract --help-extra を実行すると詳細を確認できる
builder = pyocr.builders.TextBuilder(tesseract_layout=8)
lang = 'eng'

txt = tool.image_to_string(
    img,
    lang=lang,
    builder=builder
)

print(txt)
