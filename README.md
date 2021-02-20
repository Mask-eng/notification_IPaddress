# notifIPaddress_by_python
mydns（ddnsサービス）へのIPaddress更新通知をpythonを用いて実装したもの
更新通知には、HTTP通信のPOSTを利用して行う

更新結果の成否については、Slack (channnel:mydns_update-notification )に投稿する


# 利用サービス
- MyDNS(https://www.mydns.jp/)
- Slack Incoming Webhook

# 実装
## 更新通知先URL
- https://www.mydns.jp/login.html

更新通知先URLにPOSTを行うさいに、HTTP BASIC認証を行う必要がある
HTTP BASIC認証に利用するユーザ名とパスワードは、MyDNS登録時に払い出されたものを使用する

## Slackへ投稿するPOST結果について
更新結果についての共有
- 成功した場合 -> 成功したメッセージを投稿する
- 失敗した場合 -> 失敗したメッセージとHTTP response結果内容を投稿する
