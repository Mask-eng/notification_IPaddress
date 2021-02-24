# notification_IPaddress
mydns（ddnsサービス）へのIPaddress更新通知をpythonを用いて実装したもの
更新通知には、HTTP通信のPOSTを利用して行う

更新結果の成否については、Slack (channnel:mydns_update-notification )に投稿する

# 動作環境
本スクリプトを動かすのに必要なものは下記である
- Python 3.5+.
- requests 2.12.3+

なお推奨環境としては下記としている
- Python 3.8+.
- requests 2.24+.

# 利用サービス
- MyDNS(https://www.mydns.jp/)
- Slack Incoming Webhook

# 実装
## スクリプト構成
```
notifIPaddress_by_python/
|- update_ipaddress.py		# main
|- credential.py		# .gitignore対象
|- credential.sample.py         # sample credentail configuration
```
本リポジトリに"credential.py"は含まれない
そのため、"credential.sample.py"の内容を参考に適宜設定を行う必要がある


## 更新通知先URL
- https://www.mydns.jp/login.html

更新通知先URLにPOSTを行うさいに、HTTP BASIC認証を行う必要がある
HTTP BASIC認証に利用するユーザ名とパスワードは、MyDNS登録時に払い出されたものを使用する

## Slackへ投稿するPOST結果について
更新結果についての共有
- 成功した場合 -> 成功したメッセージを投稿する
- 失敗した場合 -> 失敗したメッセージとHTTP response結果内容を投稿する
