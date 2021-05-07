# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return"Hello World."


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request #ファイル名flaskでFlaskやるよ 追加もこっちで！ *は全部！
import sqlite3
app = Flask(__name__) #アプリ名

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
    # 入力フォームから文字もらう
    task_get = request.form.get("task")
    print(task_get)
    #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #db実行
    c.execute("insert into task values(null, ?)", (task_get,))
    #DBの変更保存
    conn.commit()
    #Dbとの接続終了
    c.close()
    return "dbに保存"

# dbたすく表示
@app.route("/list")
def list():
     #データベース接続
    conn = sqlite3.connect("dbtest.db")
    #dbを操作できるように
    c = conn.cursor()
    #db実行
    c.execute("select id,name from task")
    #dbで取得したデータを変数に格納
    task_info = c.fetchall()
    print(task_info)
    #dbとの接続を終了
    c.close()
    #task_listを辞書型として宣言
    task_list = []
    #タプルから
    for item in task_info:
        task_list.append({"id": item[0], "name": item[1]})

    return render_template("list.html", tpl_task_list=task_list)






@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
