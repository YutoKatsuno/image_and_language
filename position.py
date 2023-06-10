# STEP1 画像の文字を取得する

from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use lang '%s'" % tool.get_name())


langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % lang)

img = "images/sample3.jpg"
builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
lang = 'jpn'

boxes= tool.image_to_string(
    Image.open(img),
    lang='jpn',
    builder=builder
)

for i in boxes:
    print(i)
    print(i.content)
    print(i.position)
