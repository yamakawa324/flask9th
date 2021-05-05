# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return"Hello World."


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask #ファイル名flaskでFlaskやるよ
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

@app.route("/<name>")
def greet(name):
    text = name + "さんこんにちは"
    return text





## おまじない
if __name__ == "__main__":
    app.run(debug=True)