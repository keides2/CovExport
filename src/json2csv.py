#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage: $ Python json2csv.py input.json
# #Pandasをインポート
import sys
import glob
import os
import json
import pandas as pd

# 引数１からファイル名取得
args = sys.argv
if (len(args) != 2):
    print("Usage: $ python json2csv2" + args[0] + " file name")
    quit()

file_name = args[1]
print("File name (args[1]) is %s" % file_name)
f = open(file_name)

#変換したいJSONファイルを読み込む
df = pd.read_json(f)

#CSVに変換して任意のファイル名で保存
df.to_csv(file_name + ".csv")