#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Usage: $ Python coverity-connect.py <username> <password> <id>
# 

import sys
import requests
import json

def main():
    args = sys.argv
    if (len(args) != 4):
        print("")
        print("    Usage: $ python " + args[0] + " username" + " password" + " id")
        print("")
        quit()
    
    # IDとパスワード
    USER = args[1]    # USER = "shimatani"
    PASS = args[2]    # PASS = "155807"
    # CSRF = "'09588f1c-eb5c-4e2b-b907-e81d9b7037df'"
    
    # ログイン情報
    login_info = {
        "username": USER,
        "password": PASS,
        # "_csrf": CSRF
    }
    
    # URLの設定
    url_login = "http://172.16.72.42:8080/login"
    # url_loginhtm = "http://172.16.72.42:8080/login/login.htm"
    url_logout = "http://172.16.72.42:8080/logout"

    # クッキーの名前
    cookie_name = 'COVJSESSIONID8080OP'

    # requests でログインしてセッションクッキーを作る
    session = requests.Session()    # requests.sessions.Session object at 0x7f9eefa52fd0
    
    # response = session.get(url_login)
    # response.status_code    # 200
    # responseとsessionの両方にCookieがセットされる
    # response.cookies.get('COVJSESSIONID8080OP')    # KeyError: "name='COVJSESSIONID8080OP', ...
    
    # セッションクッキーの値
    cookie_value = session.cookies.get(cookie_name)    # '163CB329FB4B4237D3F9D01667BD46AD'

    # <RequestsCookieJar[
    #  Cookie(
    #    version=0,
    #    name='COVJSESSIONID8080OP',
    #    value='163CB329FB4B4237D3F9D01667BD46AD',
    #    port=None,
    #    port_specified=False,
    #    domain='172.16.72.42',
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
    
    # r = s.get(url_login)
    
    # ログイン情報
    # r = requests.post(url_login, data=login_info)
    # r = s.post(url_login, data=login_info, cookies=COOKIES)
    r = session.post(url_login, data=login_info)
    r.url    # http://172.16.72.42:8080/reports.htm#v10174
    
    # csrf 取得
    csrf = {'X-SECURITY': '09588f1c-eb5c-4e2b-b907-e81d9b7037df'}
    COOKIES = {"COVJSESSIONID8080OP": cookie_value}
    
    # 取得したレスポンスデータをファイルに保存する
    with open('login.htm', 'w') as f:
        f.write(r.text)
    
    # URLの設定
    url_mru = "http://172.16.72.42:8080/projects/mru.json"
    url_reports = "http://172.16.72.42:8080/N2133297137.ja/bundles/reports.js"
    url_table = "http://172.16.72.42:8080/reports/table.json?viewId=10174"
    url_proj = "http://172.16.72.42:8080/projects/mru.json"
    url_source = "http://172.16.72.42:8080/sourcebrowser/source.json?projectId=10022&fileInstanceId=2747298&defectInstanceId=10251712&mergedDefectId=189485"
    
    #### mru Responseオブジェクトの生成
    res = session.get(url_mru, cookies=COOKIES)
    
    # 取得したレスポンスデータをファイルに保存する
    with open('mru.json', 'w') as f:
        f.write(res.text)
    
    # 取得したレスポンスデータをjson形式で保存する
    json_data = res.json()
    
    with open('mru2.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: mru.json")
    
    
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
    with open('source.json', 'w') as f:
        f.write(res.text)
    print("Saved: source.json")

    # 取得したレスポンスデータをjson形式で保存する
    json_data = res.json()
    # print("source_json:{}".format(json_data))

    with open('source2.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print("Saved: source2.json")

    # ログアウト
    r = session.post(url_logout, data=COOKIES)
    print("Logout:{}".format(r.url))

if __name__ == '__main__':
    main()

print("Done!")
