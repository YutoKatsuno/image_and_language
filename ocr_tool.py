# STEP2 画像の文字を取得する
# STEP3 文字の座標を取得する
from PIL import Image
import sys

import pyocr
import pyocr.builders


def get_tool():
    # 使用可能なOCRツールを取得する
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("OCRツールは見つかりませんでした")
        sys.exit(1)

    # 使うツールを返す
    return tools[0]


class OcrTool:

    def __init__(self, lang: int, path: str):
        self.tool = get_tool()
        self.lang = self.tool.get_available_languages()[lang]
        self.path = path

    # STEP2 画像の文字を取得する
    def read(self) -> str:
        img = Image.open(self.path)

        txt = self.tool.image_to_string(
            img,
            lang=self.lang,
            builder=pyocr.builders.TextBuilder(tesseract_layout=9)
        )

        return txt

    # STEP3 文字の座標を取得する
    def position(self) -> tuple:
        img = Image.open(self.path)

        pos = self.tool.image_to_string(
            img,
            lang=self.lang,
            builder=pyocr.builders.WordBoxBuilder(tesseract_layout=9)
        )

        # (x座標, y座標)を返す
        return pos[0].position[0]
