from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from re import compile
from markdown import markdown
from uuid import uuid1

# Flaskオブジェクト生成
app = Flask(__name__, static_folder='static', template_folder='templates')

# セッション
app.secret_key = 'ksjfklafjalljll' 

@app.route('/')
def index():
    text = ""
    html = ""
    switch = None
    
    if 'text' in session:
        text = session['text']
        html = session['html']
        switch = session['switch']
        
    return render_template(
        'index.html',
        text=text,
        html=html,
        switch=switch,
    )

@app.route('/input', methods=['POST'])
def input():
    
    text = request.form['md-area']
    html = markdown(text, extensions=['extra'])
    filepath = ""
    
    # 使用禁止タグを削除
    prohibited_tags = ["<script.*>", "<style.*>", "<link.*>", "<form.*>", "<input.*>", "<button.*>"]    
    for prohibited_tag in prohibited_tags:           
        regexp = compile(prohibited_tag)
        found_tags = regexp.findall(text)
        for found_tag in found_tags:
            text = text.replace(found_tag, "")
            
    # ファイル保存
    if 'cmd' in request.form:
        dir_path = './export/'
        file_name = str(uuid1())
        file_path = dir_path + file_name
        
        # MD
        if request.form['cmd'] == 'md':
            file_name += '.md'
            file_path += '.md'
            with open(file_path, 'w', newline="") as f:
                f.write(text)
            return send_from_directory(dir_path, file_name, as_attachment=True, download_name='markdown.md')
        #HTML
        if request.form['cmd'] == 'html':
            file_name += '.html'
            file_path += '.html'
            html_file = render_template('download.html', html=html)
            with open(file_path, 'w', newline="") as f:
                f.write(html_file)
            return send_from_directory(dir_path, file_name, as_attachment=True, download_name='markdown.html')
    
    # セッションに保存
    session['text'] = text
    session['html'] = html
    session['switch'] = request.form.get('switch')
    
    # index.htmlにリダイレクト
    return redirect(url_for('index', mode='writing'))