from flask import Flask, request, render_template, redirect
from flask.templating import render_template
import pymysql
from day08.daoemp import DaoEmp

app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de=DaoEmp()
    list = de.selectList()
    return render_template('emp_list.html',list=list) 

@app.route('/emp_detail')
def emp_detail():
    de=DaoEmp()
    e_id = request.args.get('e_id')
    vo = de.select(e_id)
    return render_template('emp_detail.html',vo=vo) 

@app.route('/emp_mod')
def emp_mod():
    de=DaoEmp()
    e_id = request.args.get('e_id',"null")
    vo = de.select(e_id)
    
    return render_template('emp_mod.html',vo=vo)
 
@app.route('/emp_mod_act', methods=['POST'])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    de=DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)    
    
    return render_template('emp_mod_act.html',cnt=cnt)

@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')

@app.route('/emp_add_act', methods=['POST'] )
def emp_add_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    de=DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return render_template('emp_add_act.html',cnt=cnt)

@app.route('/emp_del',methods=['POST'])
def emp_del():
    e_id = request.form['e_id']
    de=DaoEmp()
    cnt = de.delete(e_id)
    return render_template('emp_del_act.html',cnt=cnt)

    
if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')
