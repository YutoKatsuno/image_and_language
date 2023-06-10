# STEP2 画像の文字を取得する
# STEP3 文字の座標を取得する
# STEP4 文字を翻訳する
# STEP5 文字を削除する
# STEP6 翻訳したものを入れる
from greyscale import greyscale
import os

# STEP1 グレースケールする
change = input("Do you want to use the greyscale function? yes or no: ")
if change == "yes":
    # 画像の渡し方は後で変更
    img = "images/ace.jpg"
    greyscale(img)



