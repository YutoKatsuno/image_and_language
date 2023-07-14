# STEP1 グレースケールをする
import cv2
import os


# 入力: 画像のパス
# 戻り値: 新しい画像のパス or 入力画像のパス
def greyscale(img: str) -> str:

    # 名前をimages/new_〇〇の形式にする
    names = img.split("/")
    name = f"{names[0]}/new_{names[1]}"

    # すでに存在していたら入力画像のパスを返す
    is_file = os.path.isfile(name)
    if is_file:
        print("すでに同じファイルが存在しています")
        return name

    # 新しく画像を生成
    img_grey = cv2.imread(img, 0)
    cv2.imwrite(name, img_grey)
    print("新しいファイルを生成しました")

    # 新しい画像のパスを返す
    return name
