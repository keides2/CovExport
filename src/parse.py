#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Usage: $ Python parse.py <"URL of CID">
# $ python3 parse.py "http://xxx.xxx.xxx.xxx:8080/reports.htm#v10166/p10025/fileInstanceId=2867033&defectInstanceId=23898696&mergedDefectId=199751"

import sys
import requests
import json
import re
import urllib.parse

def main():
    args = sys.argv
    if (len(args) != 2):
        print("")
        print("    Usage: $ python3 " + args[0] + " \"URL of CID\"")
        print("")
        quit()
    
    URL = args[1]       # URL = "http://xxx.xxx.xxx.xxx:8080/reports.htm#v10166/p10025/fileInstanceId=2867033&defectInstanceId=23898696&mergedDefectId=199751"
    
    # パースしたURL
    print("url: \n")
    print(urllib.parse.urlparse(URL))
    
    # クエリー抽出
    qs = urllib.parse.urlparse(URL).fragment
    print("fragment: \n")
    print(qs)
    
    # クエリ文字列を辞書に変換
    qs_d = urllib.parse.parse_qs(qs)
    print("辞書: \n")
    print(qs_d)                                     # {'v10166/p10025/fileInstanceId': ['2867033'], 'defectInstanceId': ['23898696'], 'mergedDefectId': ['199751']}
    print(qs_d['v10166/p10025/fileInstanceId'])     # ['2867033']
    print(qs_d['v10166/p10025/fileInstanceId'][0])  # 2867033
    print("\n")
    print(qs_d['defectInstanceId'])                 # ['23898696']
    print(qs_d['defectInstanceId'][0])              # 23898696
    print("\n")
    print(qs_d['mergedDefectId'])                   # ['199751']
    print(qs_d['mergedDefectId'][0])                # 199751
    print("\n")

    # クエリ文字列をリストに変換
    qs_l = urllib.parse.parse_qsl(qs)
    print("リスト: \n")
    print(qs_l)                                     # [('v10166/p10025/fileInstanceId', '2867033'), ('defectInstanceId', '23898696'), ('mergedDefectId', '199751')]
    print(qs_l[0])                                  # ('v10166/p10025/fileInstanceId', '2867033')
    
    qs_l_0 = qs_l[0][0]                             # ('v10166/p10025/fileInstanceId', '2867033')
    list = qs_l_0.split("/")                        # v10166, p10025, fileInstanceId
    VIEWID = list[0].replace('v', '')               # 10166
    PROJECTID = list[1].replace('p', '')            # 10025
    FILEINSTANCEID =qs_l[0][1]                      # 2867033
    
    print(VIEWID)
    print(PROJECTID)
    print(FILEINSTANCEID)
    
    print("\n")
    print(qs_l[1])
    print("defectInstanceId = {}".format(qs_l[1][1]))
    print("\n")
    print(qs_l[2])
    print("mergedDefectId = {}".format(qs_l[2][1]))
    print("\n")

if __name__ == '__main__':
    main()

print("Done!")
