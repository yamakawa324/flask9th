# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return"Hello World."


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, session #ファイル名flaskでFlaskやるよ 追加もこっちで！ *は全部！
import sqlite3, random #randomはFlaskのあとに書いたら作用しなくなる
app = Flask(__name__) #アプリ名

#暗号化の秘密鍵を作成 ””の間はランダムで
app.secret_key = "sunabaco"

@app.route('/') #/にアクセスした時に、下の関数を動かす
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route("/top")
def top():
    text = "ここはトップページです"
    return text

# @app.route("/<name>")
# def greet(name):
#     text = name + "さんこんにちは"
#     return text

@app.route("/tpltest/<name>")
def tpltest(name):
    return render_template("index.html", tpl_name=name)

@app.route("/profile")
def profile():
    name = "やまかわさと"
    ago = 27
    address = "うるま市宮里842ー３"
    return render_template("profile.html", tpl_name=name, tpl_ago=ago, tpl_address=address)

@app.route("/weathre")
def weathre():
    weathre1 = "晴れ"
    return render_template("weathre.html", tpl_weather1=weathre1 )

@app.route("/dbtest")
def dbtest():
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #db実行
    c.execute("select name,age,address from users where id = 2")
    #dbで取得したデータを変数に格納
    user_info = c.fetchone()
    print(user_info)
    #dbとの接続を終了
    c.close()
    return render_template("dbtest.html", tpl_name=user_info[0],tpl_age=user_info[1],tpl_address=user_info[2])

@app.route("/addpage") 
def addpage():
    return render_template("add.html")

# POSTメソッド入力フォームからデータ送信
@app.route("/add", methods=["POST"])
def add():
    #クッキーに保存されているuseridを受け取る
    user_id_py = session["user_id"]
    # 入力フォームから文字もらう
    task_get = request.form.get("task")
    print(task_get)
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #db実行
    c.execute("insert into task values(null, ?, ?)", (task_get, user_id_py))
    #DBの変更保存
    conn.commit()
    #Dbとの接続終了
    c.close()
    #/listにリダイレクト インポートしないとできないよ
    return redirect("/list")


@app.route("/color")
def color():
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #db実行
    c.execute("select name from color")
    #dbで取得したデータを変数に格納
    color = c.fetchall() #hallはDBすべての情報をとってくる
    c.close()
    print(color)
    #ランダムで色を一つ選ぶ
    color_choice = random.choice(color)
    return render_template("color.html", html_color=color_choice[0])

@app.route("/add_get") #ここにアクセスしたら下のプログラム動かすよ
def add_get():
    return render_template("add.html") #HTMLを表示するよ

@app.route("/add_post",methods=["post"])
def add_post():
    #HTMLの入力フォームから受け取る
    py_task = request.form.get("html_task")
    print(py_task)
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #dbに値を挿入するSQLのコードをかく
    c.execute("insert into task2 values(null, ?)",(py_task,)) #nullのあとに変数名を入れると文字として処理される、ので？ その後 , 変数名を入れる
    #dbに変更を加えたんで保存
    conn.commit()
    c.close()
    return redirect("/list") #自動でページに飛ばしてくれる

#DBに登録されている文字を表示する
@app.route("/list")
def li():
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #dbから値をTASKテーブルより取得
    c.execute("select id,name from task2")
    #dbで取得したデータを変数に格納
    py_task = c.fetchall() #hallはDBすべての情報をとってくる
    c.close()
    print(py_task)
    #格納用の変数(リスト型)を用意
    task_list = []
    #dbから持ってきたデータをすべて追加してゆく
    for item in py_task:
        #tasl
        task_list.append({"id": item[0], "name": item[1]})
    return render_template("list.html", html_task=task_list)

@app.errorhandler(404)
def not_found(error):
    return "お探しのページはない"








## おまじない
if __name__ == "__main__":
    app.run(debug=True)
