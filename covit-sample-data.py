#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:01:14 2023

@author: kozakikakeru
"""
import cv2
import pandas as pd
import math

def measure_contour_properties(image_path):
    # 画像の読み込み
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 2値化処理
    _, threshold = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    
    #反転
    inverted = cv2.bitwise_not(threshold)

    # 輪郭の検出
    contours, _= cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 結果を保存するデータフレームを作成
    data = {
        '面積': [],
        '周囲長': [],
        '真円度': [],
        'フェレ比': [],
        '面積比': [],
        'フェレ比2':[]
    }

    # 各輪郭に対して計測
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = 4 * math.pi * area / (perimeter ** 2)
        feret_ratio = cv2.minEnclosingCircle(contour)[1] / cv2.minAreaRect(contour)[1][1]
        bounding_rectangle = cv2.minAreaRect(contour)[1][0]*cv2.minAreaRect(contour)[1][1]
        x, y, w, h = cv2.boundingRect(contour)

        # データをデータフレームに追加
        data['面積'].append(area)
        data['周囲長'].append(perimeter)
        data['真円度'].append(circularity)
        data['フェレ比'].append(feret_ratio)
        data['面積比'].append(area / bounding_rectangle)
        data['フェレ比2'].append((w-1)/(h-1))

    # データフレームを作成
    df = pd.DataFrame(data)
    
    print(df)

    # 結果をExcelファイルに保存
    output_path = "measurement_results.xlsx"
    df.to_excel(output_path, index=False)

    print("計測結果をExcelファイルに保存しました:", output_path)
    
    print(len(contours))

# 画像ファイルのパス
image_path = "sample.png"

# 輪郭のプロパティを計測し、結果をExcelファイルに保存
measure_contour_properties(image_path)

