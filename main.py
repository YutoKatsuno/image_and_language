# STEP5 文字を削除する
# STEP6 翻訳したものを入れる
from greyscale import greyscale
from ocr_tool import OcrTool
from translate import translate

lang = input("Is the image in 'English' or 'Japanese'?\nPlease enter: ")
# 英語は0、日本語は1
if lang == "English":
    kind_of_lang = 0
else:
    kind_of_lang = 1

# STEP1 グレースケールする
change = input("Do you want to use the greyscale function? yes or no: ")
img = "images/" + input("Where is your image file? images/")
if change == "yes":
    img = greyscale(img)
print(img)

# STEP2 画像の文字を取得する
ocr_tool = OcrTool(kind_of_lang, img)
img_lang = ocr_tool.read()
print(img_lang)

# STEP3 文字の座標を取得する
xy = ocr_tool.position()
print(xy)

# STEP4 文字を翻訳する
a = translate(kind_of_lang, img_lang)
print(a)
