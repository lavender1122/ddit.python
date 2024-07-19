from flask import Flask, request, redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("static/ex07.html")


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
