from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day12.daoemp import DaoEmp
import time

app = Flask(__name__) 

@app.route('/')   
def main(): 
    return redirect("static/async.html")

@app.route('/get1', methods=['POST'])  
def get1(): 
    # time.sleep(1)#1초 시간정지
    return jsonify(num = 1)
@app.route('/get2', methods=['POST'])  
def get2(): 
    return jsonify(num = 2)

if __name__ == '__main__': 
    app.run(debug=True, port=80, host='0.0.0.0')
    
    
    
    