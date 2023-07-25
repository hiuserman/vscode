#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:55:18 2023

@author: kozakikakeru
"""

import cv2

def count_black_spots(image_path,output_path):
    # 画像の読み込み
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    image2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 2値化処理
    _, threshold = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    
    #反転
    inverted = cv2.bitwise_not(threshold)

    # 輪郭の検出
    #contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _= cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 輪郭を描画
    image2=cv2.drawContours(threshold, contours, 3, color=(0,230,233), thickness=2)
    
    # 画像表示用に入力画像をカラーデータに変換する
    img_disp = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)

    # 全ての輪郭を描画
    cv2.drawContours(img_disp, contours, -1, (0, 0, 255), 2)

    # 輪郭の点の描画
    #for contour in contours:
    #    for point in contour:
    #        cv2.circle(img_disp, point[0], 1, (0, 255, 0), -1)

    # 輪郭が描かれた画像を保存
    cv2.imwrite(output_path, img_disp)

    # 斑点の数を返す
    return len(contours)

# 画像ファイルのパス
image_path = 'sample.png'

output_path='output.png'

# 黒い斑点の数を数える
count = count_black_spots(image_path,output_path)

# 結果の出力
print("黒い斑点の数:", count)
