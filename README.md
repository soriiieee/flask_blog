# 参考
公式document：　https://flask.palletsprojects.com/en/1.1.x/quickstart/
Youtube：
1. get started
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
2. ログインフォームの作成
https://www.youtube.com/watch?v=UIJKdCIEXUQ
### app.config["SECRET_KEY"] = 'c0cee159c47e87bca14994d2d7577cc0'
`python`
`>> import secrets`
`>> secrets.token_hex(16)`


#　install
1.初期設定 
`pip install flask`

2.ログイン画面等
`pip install flask-wtf` ログイン画面のテンプレートapi
`pip install email-validator` email validatorのため、つかで必要なモジュール軍
参考[flask-wtfの使い方](https://qiita.com/tbpgr/items/989c6badefff69377da7)

