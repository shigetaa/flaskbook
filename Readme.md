# Flask開発

## Flask 環境構築
### Python 仮想環境を設定する
```bash
python -m venv venv
source venv/bin/activate
```
### Flask インストール
```bash
pip install flask
```
#### Flask が依存しているパッケージ
```bash
pip list
```
```
Package            Version
------------------ -------
blinker            1.6.2
click              8.1.7
Flask              2.3.3
importlib-metadata 6.8.0
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.3
pip                21.2.3
setuptools         53.0.0
Werkzeug           2.3.7
zipp               3.16.2
```
#### ライブラリのインストール
```bash
pip install flake8 black isort mypy
```
|ライブラリ名|用途|
|:--|:--|
|flake8|PEP8に沿った書き方のコードかどうかを自動チェック|
|black|PEP8に沿った書き方にコードが自動整形|
|isort|import文をPEP8に沿った書き方に自動並び替え|
|mypy|タイプヒントの型チェック|

#### Flask コマンド
Flask をインストールすると、`flask` コマンドが使えます。
##### flask run
`flask run` コマンドを実行すると、開発用Webサーバーが起動します。
コマンドを実行するにあたり、環境変数 `FLASK_ENV` を指定しない場合エラーで
開発用Webサーバーは起動しません。
```bash
vim app.py
```
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask book!"
```
環境変数 `FLASK_ENV=development` として `development` を指定した場合、デバックモードとして
エラー情報、オートリロードなどが有効になり、開発をしやすい用になります。

本番環境では、`production` を指定します。
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

##### flask routes
`flask routes` コマンドを実行すると、アプリのルーティング情報を出力します。
```bash
flask routes
```
```bash
Endpoint  Methods  Rule                   
--------  -------  -----------------------
index     GET      /                      
static    GET      /static/<path:filename>
```

##### .env を使用して環境変数を設定する
```bash
pip install python-dotenv
```
```bash
vim .env
```
```env
FLASK_APP=app.py
FLASK_ENV=development
```
