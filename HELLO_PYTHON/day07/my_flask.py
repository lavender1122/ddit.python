from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/param',methods=['GET'])
def param():
    menu = request.args.get('menu', "default")
    return 'PARAM:' + menu

# post,get 방식 둘다 됨
@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        menu = request.form['menu']
        return 'post:' + menu
    else:
        return 'GET request'

@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치", "장화홍련"]
    return render_template('forw.html', a=a, b=b)

@app.route('/emp')
def emp():
    mylist = [
        {'e_id': '1', 'e_name': '1', 'gen': '1', 'addr': '1'},
        {'e_id': '2', 'e_name': '2', 'gen': '2', 'addr': '2'},
        {'e_id': '3', 'e_name': '3', 'gen': '3', 'addr': '3'}
    ]
    return render_template('emp.html', mylist=mylist)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
