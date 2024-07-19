from flask import Flask,request,redirect,jsonify
from flask.templating import render_template
from day12.daoemp import DaoEmp
import time

app = Flask(__name__) 

@app.route('/')   
def main(): 
    return 'Hello Docker'


if __name__ == '__main__': 
    app.run(debug=True, port=80, host='0.0.0.0')
    
    
    
    