#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Usage: $ Python connect.py <username> <password> <viewId> <projectId> <CID>
# 

import sys
import requests
import json
import re

def main():
    args = sys.argv
    if (len(args) != 6):
        print("")
        print("    Usage: $ python " + args[0] + " username" + " password" + " viewId" + " ProjectId" + " CID")
        print("")
        quit()
    
    # IDとパスワード
    USER = args[1]      # USER = "hoge"
    PASS = args[2]      # PASS = "******"
    VIEWID = args[3]    # viewId = "10174"
    PROJID = args[4]    # ProjectID  "10025" 
    CID = args[5]       # CID = "199756"
    # CSRF = "'09588f1c-eb5c-4e2b-b907-e81d9b7037df'"
    
    # ログイン情報
    login_info = {
        "username": USER,
        "password": PASS,
        # "_csrf": CSRF
    }
    
    # URLの設定
    url_login = "http://xxx.xxx.xxx.xxx:8080/login"
    # url_loginhtm = "http://xxx.xxx.xxx.xxx:8080/login/login.htm"
    url_logout = "http://xxx.xxx.xxx.xxx:8080/logout"

    # ログイン
    # response = session.get(url_login)
    # response.status_code    # 200
    # responseとsessionの両方にCookieがセットされる
    # response.cookies.get('COVJSESSIONID8080OP')    # KeyError: "name='COVJSESSIONID8080OP', ...

    # requests でログインしてセッションクッキーを作る
    session = requests.Session()    # requests.sessions.Session object at 0x7f9eefa52fd0
    
    # r = requests.post(url_login, data=login_info)
    # r = s.post(url_login, data=login_info, cookies=COOKIES)
    r = session.post(url_login, data=login_info)
    r.url    # http://xxx.xxx.xxx.xxx:8080/reports.htm#v10174
    
    # 取得したレスポンスデータをファイルに保存する
    with open('login.htm', 'w') as f:
        f.write(r.text)
    
    # クッキーの名前
    cookie_name = 'COVJSESSIONID8080OP'

    # セッションクッキーの値
    cookie_value = session.cookies.get(cookie_name)    # '163CB329FB4B4237D3F9D01667BD46AD'
    print("Cookie_Value: {}".format(cookie_value))
    
    # >>> session.cookies
    # <RequestsCookieJar[
    #  Cookie(
    #    version=0,
    #    name='COVJSESSIONID8080OP',
    #    value='163CB329FB4B4237D3F9D01667BD46AD',
    #    port=None,
    #    port_specified=False,
    #    domain='xxx.xxx.xxx.xxx',
    #    domain_specified=False,
    #    domain_initial_dot=False,
    #    path='/',
    #    path_specified=True,
    #    secure=False,
    #    expires=None,
    #    discard=True,
    #    comment=None,
    #    comment_url=None,
    #    rest={'HttpOnly': None},
    #    rfc2109=False
    #  )
    # ]>
    
    # csrf 取得
    # csrf = {'X-SECURITY': '09588f1c-eb5c-4e2b-b907-e81d9b7037df'}
    COOKIES = {cookie_name: cookie_value}

    # URLの設定
    url_mru = "http://xxx.xxx.xxx.xxx:8080/projects/mru.json"
    url_reports = "http://xxx.xxx.xxx.xxx:8080/N2133297137.ja/bundles/reports.js"
    # url_table = "http://xxx.xxx.xxx.xxx:8080/reports/table.json?viewId=10174"
    url_table = "http://xxx.xxx.xxx.xxx:8080/reports/table.json?viewId=" + VIEWID
    url_proj = "http://xxx.xxx.xxx.xxx:8080/projects/mru.json"
    
    # CID別の指摘
    # url_source = "http://xxx.xxx.xxx.xxx:8080/sourcebrowser/source.json?projectId=10022&fileInstanceId=2747298&defectInstanceId=10251712&mergedDefectId=189485"
    
    # GPF専用
    # ↓はブラウザのアドレスだがエラーが出る
    # url_source = "http://xxx.xxx.xxx.xxx:8080/reports.htm#v10166/p10025/fileInstanceId=2873414&defectInstanceId=24188432&mergedDefectId=200542"
    
    # fileInstanceIdとdefectInstanceIdが取得できないので、ブラウザを開いて手作業で取得する
    # url_source = "http://xxx.xxx.xxx.xxx:8080/sourcebrowser/source.json?projectId=10025&fileInstanceId=2871726&defectInstanceId=24188311&mergedDefectId=200541"
    # url_source = "http://xxx.xxx.xxx.xxx:8080/sourcebrowser/source.json?projectId=10025&fileInstanceId=2873414&defectInstanceId=24188432&mergedDefectId=200542"
    url_source = "http://xxx.xxx.xxx.xxx:8080/sourcebrowser/source.json?projectId=10025&fileInstanceId=2852728&defectInstanceId=22455742&mergedDefectId=" + CID
    # print("url_source:")
    # print(url_source)
    # exit()
    
    #### mru Responseオブジェクトの生成
    res = session.get(url_mru, cookies=COOKIES)
    
    # 取得したレスポンスデータをファイルに保存する
    with open('mru.json', 'w') as f:
        f.write(res.text)
    print("Saved: mru.json")
    
    # 取得したレスポンスデータをjson形式で保存する
    json_data = res.json()
    
    with open('mru2.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: mru2.json")
    
    
    #### reports Responseオブジェクトの生成
    res = session.get(url_reports, cookies=COOKIES)
    
    # 取得したレスポンスデータをファイルに保存する
    with open('reports.js', 'w') as f:
        f.write(res.text)
    print("Saved: reports.js")
    
    
    #### table Responseオブジェクトの生成
    res = session.get(url_table, cookies=COOKIES)
    # print("\ntable: {}".format(res.text))
    
    
    # 取得したレスポンスデータをファイルに保存する
    with open('table.json', 'w') as f:
        f.write(res.text)
    print("Saved: table.json")

    # 取得したレスポンスデータをjson形式で保存する
    json_data = res.json()
    
    with open('table2.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: table2.json")
    
    
    #### source Responseオブジェクトの生成
    res = session.get(url_source, cookies=COOKIES)
    # print("source: {}".format(res.text))
    
    # 取得したレスポンスデータをファイルに保存する
    with open('source-' + CID + '.json', 'w') as f:
        f.write(res.text)
    print("Saved: source-" + CID + ".json")

    # 取得したレスポンスデータをjson形式で保存する
    json_data = res.json()
    # print("source_json:{}".format(json_data))

    with open('source2-' + CID + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: source2-" + CID + ".json")

    # extract.py から移植　必要な行を抜き出してタグを削除する
    source = 'source2-' + CID + '.json'
    with open(source) as f:
        lines = f.readlines()
    
    l_extract = [line for line in lines if ('cid' in line) or ('mainEventId' in line) or ('events' in line) or ('shortDescription' in line) or ('description' in line) or ('lineNumber' in line)]
    
    # for line in l_extract:
    #     print(line)

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

    # ログアウト
    r = session.post(url_logout, data=COOKIES)
    # print("Logout:{}".format(r.url))  # Logout:http://xxx.xxx.xxx.xxx:8080/login/login.htm

if __name__ == '__main__':
    main()

print("Done!")
