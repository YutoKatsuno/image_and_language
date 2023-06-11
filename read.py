# STEP2 画像の文字を取得する
from PIL import Image
import sys

import pyocr
import pyocr.builders


def read(path):

    # 使用可能なOCRツールを取得する
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("OCRツールは見つかりませんでした")
        sys.exit(1)

    # 使うツールを選ぶ
    tool = tools[0]

    # 日本語がインストールされていない場合はここから
    # https://github.com/tesseract-ocr/tessdata/raw/4.00/jpn.traineddata
    # https://github.com/tesseract-ocr/tessdata_best/blob/main/jpn_vert.traineddata
    # homebrewを使っている場合は/opt/homebrew/Cellar/tesseract/5.2.0/share/tessdata/にダウンロードしたファイルを移動させる
    langs = tool.get_available_languages()
    lang = langs[0]

    img = Image.open(path)
    # 何も表示されていない時はtesseract_layoutの値を調整する
    # tesseract --help-extra を実行すると詳細を確認できる
    builder = pyocr.builders.TextBuilder(tesseract_layout=8)

    txt = tool.image_to_string(
        img,
        lang=lang,
        builder=builder
    )

    print(txt)

