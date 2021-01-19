#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Usage: $ Python json-parse.py <filename>
# e.g.
# $ python3 json-parse.py table.json

import sys
import os
import json

def main():
    args = sys.argv
    if (len(args) != 2):
        print("")
        print("    Usage: $ python3 " + args[0] + " filename")
        print("")
        quit()
    
    filepath = args[1]
    basename = os.path.basename(filepath)
    basename_without_ext = os.path.splitext(basename)[0]
    
    # json形式で読み込む
    with open(filepath) as f:
        json_data = json.load(f)
    
    # json形式で保存する
    with open(basename_without_ext + '2.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: basename_without_ext + '2.json'")
    
if __name__ == '__main__':
    main()

print("Done!")
