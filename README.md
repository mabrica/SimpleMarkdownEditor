# SimpleMarkdownEditor

『Simple Markdown Editor』 はブラウザ上で手軽に使える簡易的なマークダウンエディタです。

---

## 使用しているフレームワーク・ライブラリ

- Python
    - Flask
    - Python-Markdown


- JavaScript
    - JQuery
    - jquery-pwd-measure

---

## ローカルでの実行方法
1. ShutterDiaryフォルダの直下に仮想環境を構築します。
    > python -m venv .venv 

2. 仮想環境を実行します。
    - Mac
        > source .venv/bin/activate 

    - Windows
        > .venv\Scripts\activate.bat
3. 必要なライブラリをインストールします。
    >pip install -r requirements.txt
4. 簡易サーバーを立ち上げます。
    - Mac
        >export FLASK_APP=flask_app  
        >flask run
    - Windows
        >set FLASK_APP=flask_app  
        >flask run
5. 表示されたURLにWebブラウザからアクセスします。
