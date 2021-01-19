# from bs4 import BeautifulSoup
import requests
import pprint
import json

# IDとパスワード
USER = "shimatani"
PASS = "155807"
CSRF = "'09588f1c-eb5c-4e2b-b907-e81d9b7037df'"

# ログイン情報
login_info = {
    "username": USER,
    "password": PASS,
    "_csrf": CSRF
    }

# URLの設定
url_login = "http://172.16.72.42:8080/login"
url_loginhtm = "http://172.16.72.42:8080/login/login.htm"
url_logout = "http://172.16.72.42:8080/logout"

# クッキーの名前
cookie_name = 'COVJSESSIONID8080OP'

# requests でログインしてセッションクッキーを作る
session = requests.Session()　　　　# requests.sessions.Session object at 0x7f9eefa52fd0

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

# r.raise_for_status()

# csrf 取得
csrf = {'X-SECURITY': '09588f1c-eb5c-4e2b-b907-e81d9b7037df'}
COOKIES = {'COVJSESSIONID8080OP': 'D0C84A6A3445BE075DEB7DC82469B97B'}
COOKIES = {"COVJSESSIONID8080OP": "D866FF1B4FC8CE6B61C92528113089C3"}
COOKIES = {"COVJSESSIONID8080OP": "0318427648150B355532A7DE300E72F0"}
COOKIES = {"COVJSESSIONID8080OP": cookie_value}

# 取得したレスポンスデータをファイルに保存する
with open('login.htm', 'w') as f:
    f.write(r.text)

# URLの設定
url_reports = "http://172.16.72.42:8080/N2133297137.ja/bundles/reports.js"
url_mru = "http://172.16.72.42:8080/projects/mru.json"
url_table = "http://172.16.72.42:8080/reports/table.json?viewId=10174"
url_proj = "http://172.16.72.42:8080/projects/mru.json"
url_source = "http://172.16.72.42:8080/sourcebrowser/source.json?projectId=10022&fileInstanceId=2747298&defectInstanceId=10251712&mergedDefectId=189485"

# mru Responseオブジェクトの生成
res = session.get(url_mru, cookies=COOKIES)
# 取得したレスポンスデータをファイルに保存する
with open('mru.json', 'w') as f:
    f.write(res.text)
# 取得したレスポンスデータをjson形式で保存する
json_data = res.json()
with open('mru2.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

# reports Responseオブジェクトの生成
res = session.get(url_reports, cookies=COOKIES)
# 取得したレスポンスデータをファイルに保存する
with open('reports.json', 'w') as f:
    f.write(res.text)
# 取得したレスポンスデータをjson形式で保存する
json_data = res.json()
with open('reports2.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

# table Responseオブジェクトの生成
res = session.get(url_table, cookies=COOKIES)
# 取得したレスポンスデータをファイルに保存する
with open('table.htm', 'w') as f:
    f.write(res.text)
# 取得したレスポンスデータをjson形式で保存する
json_data = res.json()
with open('table2.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

# source Responseオブジェクトの生成
res = session.get(url_source, cookies=COOKIES)
# 取得したレスポンスデータをファイルに保存する
with open('source.json', 'w') as f:
    f.write(res.text)
# 取得したレスポンスデータをjson形式で保存する
json_data = res.json()
with open('source2.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

# pprint.pprint(json_data, depth=10, compact=True)
# pprint.pprint(json_data['resultSet']['results']['15']['project'])    # iTM HTML5
# pprint.pprint(json_data['resultSet']['results']['16']['project'])    # ERMS
str = pprint.pformat(json_data['resultSet']['results']['16']['project'])


    
# ログアウト
r = s.post(url_login, data=COOKIES)
r.headers['Set-Cookie']
# 'Set-Cookie': 'COVJSESSIONID8080OP=BABE99579F51C88AD3D7785A17929B1E; Path=/; HttpOnly',
# ログイン
r = s.post(url_login, data=login_info)

r = s.get(url_loginhtm, cookies={"COVJSESSIONID8080OP": "D866FF1B4FC8CE6B61C92528113089C3"})

headers = {'Cookie': 'BABE99579F51C88AD3D7785A17929B1E'}
r = s.get(url_loginhtm, headers=headers)


'''
# トークンを取得する場合
payload = {
    'utf8': '✓',
    'identity': 'username or email',
    'password': 'secret'
}

# セッションを開始
s = requests.Session()
r = s.get('https://qiita.com')
soup = BeautifulSoup(r.text)
auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
payload['authenticity_token'] = auth_token

# ログイン
s.post('https://qiita.com/login', data=payload)

# URLの設定
url2 = "http://172.16.72.42:8080/sourcebrowser/source.json?projectId=10022&fileInstanceId=2747298&defectInstanceId=10251712&mergedDefectId=189485"

# パラメータの設定
param = { "format": "json",
     "action": "query",
     "prop": "revisions",
     "titles": "日本酒",
     "rvprop": "content",
     "rvparse":""}
 
# Responseオブジェクトの生成
# res = requests.get(url, params=param)
res = requests.get(url2)

# レスポンスの中身（最初の200文字）
res.text

# ヘッダ
res.headers

# URLの確認
res.url

# ステータスコードのチェック
res.status_code

# HTTPステータスの理由
res.reason

# 正常にアクセスできた場合
res = requests.get('https://hibiki-press.tech/learn_prog/')
# HTTPErrorが発生していないので、Noneを返す
res.raise_for_status()

# 存在しないページにアクセスした場合、、
no_exist = requests.get('https://hibiki-press.tech/no_exist/')
# HTTPErrorが送出される
no_exist.raise_for_status()
Traceback (most recent call last):
File "", line 1, in
File "/home/hibikisan/anaconda3/envs/python3.7/lib/python3.7/site-packages/requests/models.py", line 939, in raise_for_status
raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://hibiki-press.tech/learn_prog/no_exist/

def url_check(url):
	try:
		res = requests.get(url)
		res.raise_for_status()
		＃ リクエストが成功したらＯＫを表示
		print('OK')
	except requests.RequestException as e:
		＃ エラーが発生したら、その内容を表示
		print(e)

# 存在しないページの場合
>>> url_check('https://hibiki-press.tech/no_exist')
404 Client Error: Not Found for url: https://hibiki-press.tech/learn_prog/no_exist

＃ドメインが存在しない場合
>>> url_check('https://hibiki-press.xxx')
HTTPSConnectionPool(host='hibiki-press.xxx', port=443): Max retries exceeded with url: / (Caused by NewConnectionError(': Failed to establish a new connection: [Errno -2] Name or service not known',))

# 正常にアクセスできた場合
url_check('https://hibiki-press.tech/learn_prog')
OK

# カスタムヘッダーの付与
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://api.github.com/some/endpoint', headers=headers)

# 以下URLがCookieを返却する場合には
r = requests.get('http://example.com/some/cookie/setting/url')

# 以下のようにCookieを取得できます.
print(r.cookies['example_cookie_name']) # 'example_cookie_value'

# Cookieを付与してHTTP通信を行う
cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text) # '{"cookies": {"cookies_are": "working"}}'

# CookieJarを用いて、より詳細にCookieを指定することもできます.
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
r = requests.get('http://httpbin.org/cookies', cookies=jar)
print(r.text) # '{"cookies": {"tasty_cookie": "yum"}}'
'''