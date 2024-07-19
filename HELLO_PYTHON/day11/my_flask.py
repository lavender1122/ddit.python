from flask import Flask, request, redirect,url_for,jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return redirect("static/jq01.html")

@app.route('/ajax' ,methods=['post'])
def ajax():
    date=request.get_json()
    print(date['menu'])
    return jsonify(result = "success", result2= date)
    
@app.route('/axios' ,methods=['post'])
def axios():
    data=request.get_json()
    print(data['menu'])
    return jsonify(message="ok")

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
