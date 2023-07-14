# STEP4 文字を翻訳する
# STEP5 文字を削除する
# STEP6 翻訳したものを入れる
from greyscale import greyscale
from ocr_tool import OcrTool

lang = input("Is the image in 'English' or 'Japanese'?\nPlease enter: ")
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
print(ocr_tool.read())
# # STEP3 文字の座標を取得する
n = ocr_tool.position()
print(n)
print(type(n))
