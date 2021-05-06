# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return"Hello World."


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template #ファイル名flaskでFlaskやるよ 追加もこっちで！ *は全部！
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

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
