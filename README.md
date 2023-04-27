# SimpleMarkdownEditor

『Simple Markdown Editor』 はブラウザ上で手軽に使える簡易的なマークダウンエディタです。

<br>

### 使用しているフレームワーク・ライブラリ

- Python
    - Flask
    - Python-Markdown


- JavaScript
    - JQuery
    - jquery-pwd-measure
    
<br>

### ローカルでの実行方法
1. SimpleMarkdownEditorフォルダの直下に仮想環境を構築します。
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

<br>

---

<br>

# SimpleMarkdownEditor

_Simple Markdown Editor_ is a web app where you can easily edit markdown texts on your web browser.

<br>

### Used Frameworks and Libraries

- Python
    - Flask
    - Python-Markdown


- JavaScript
    - JQuery
    - jquery-pwd-measure

<br>

### How to run locally
1. Create an virtual enviroment directly under SimpleMarkdownEditor folder.
    > python -m venv .venv 

2. Activate the virtual enviroment.
    - Mac
        > source .venv/bin/activate 

    - Windows
        > .venv\Scripts\activate.bat
        
3. Install all required libraries.
    >pip install -r requirements.txt
    
4. Run the builtin server.
    - Mac
        >export FLASK_APP=flask_app  
        >flask run
    - Windows
        >set FLASK_APP=flask_app  
        >flask run
        
5. Access the displayed URL using a web browser.
