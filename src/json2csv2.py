#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage: $ Python json2csv.py input.json
# Pandas をインポート
import sys
import glob
import os
import json
import pandas as pd

# 引数チェック
args = sys.argv
if (len(args) != 2):
    print("Usage: $ python json2csv2" + args[0] + " file name with extention")
    quit()

# 引数１からファイル名取得
file_name = args[1]
print("File name (args[1]) is %s" % file_name)

# 拡張子ありのファイル名
basename = os.path.basename(file_name)

# 拡張子なしのファイル名
basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]

# 整形してjson形式で保存する
with open(file_name) as file:
    json_data = json.load(file)

with open(basename_without_ext + "2.json", 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
print("Saved: " + basename_without_ext + "2.json")

# 方法１
# 変換したいJSONファイルを読み込む
# df = pd.read_json(f)

# CSVに変換して任意のファイル名で保存
# df.to_csv(basename_without_ext + ".csv")

# 方法2
# 変換したいJSONファイルを読み込む
f = open(basename_without_ext + "2.json")
df2 = json.load(f)
jsondt = pd.DataFrame(df2)

#CSVに変換して任意のファイル名で保存
jsondt.to_csv(basename_without_ext + "2.json" + ".csv")

f.close()

