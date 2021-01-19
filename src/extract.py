#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Usage: $ Python extract.py <CID>
# 

import sys
import requests
import json
import re

def main():
    args = sys.argv
    if (len(args) != 2):
        print("")
        print("    Usage: $ python " + args[0] + " CID")
        print("")
        quit()
    
    CID = args[1]       # CID = "199756"
    
    source = 'source2-' + CID + '.json'
    with open(source) as f:
        lines = f.readlines()
    
    l_extract = [line for line in lines if ('cid' in line) or ('mainEventId' in line) or ('events' in line) or ('shortDescription' in line) or ('description' in line) or ('lineNumber' in line)]
    
    for line in l_extract:
        print(line)

    # ファイルに保存する
    with open('source3-' + CID + '.txt', 'w') as f:
        for line in l_extract:
            f.write(line)
            
    print("Saved: source3-" + CID + ".txt")
    
    # タグを削除してファイルに保存する
    with open('source4-' + CID + '.txt', 'w') as f:
        for line in l_extract:
            f.write(re.sub('<[^>]*>', '', line))
            
    print("Saved: source4-" + CID + ".txt")

if __name__ == '__main__':
    main()

print("Done!")
