#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage: $ Python format-json.py input.json
# 
import sys
import glob
import os
import json

# メイン
def main():
    # 引数１からファイル名取得
    args = sys.argv
    if (len(args) != 2):
        print("Usage: $ python" + args[0] + " file name")
        quit()

    file_name = args[1]
    # print("File name (args[1]) is %s" % file_name)

    f = open(file_name)
    json_dict = json.load(f)
    print('json_dict:{}'.format(type(json_dict)))
    # print('json_dict: projects:{}'.format(json_dict['projects']['name']))
    for x in json_dict:
        print('{0}:{1}'.format(x, json_dict[x]))

if __name__ == '__main__':
	main()

print("----- Done!")