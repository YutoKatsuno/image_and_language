# STEP1 グレースケールをする
import cv2
import os


def greyscale(img):

    # 名前をimages/new_〇〇の形式にする
    names = img.split("/")
    name = f"{names[0]}/new_{names[1]}"

    # すでに存在していたら終了
    is_file = os.path.isfile(name)
    if is_file:
        # 開発が終わった時に削除
        print("すでに同じファイルが存在しています")
        return

    # 画像の読み込み
    img_grey = cv2.imread(img, 0)

    # 新しく画像を生成
    cv2.imwrite(name, img_grey)
    # 開発が終わった時に削除
    print("新しいファイルを生成しました")
    return
