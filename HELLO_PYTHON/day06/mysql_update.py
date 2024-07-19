import pymysql
con = pymysql.connect(host='localhost', user='root', port=3305
                       ,password='python', db='python', charset='utf8')
# cur = conn.cursor(pymysql.cursors.DictCursor)
cur = con.cursor()
e_id="3"
e_name="6"
gen="6"
addr="6"


query = f'''
       update emp
       set
           e_name='{e_name}',
           gen='{gen}',
           addr='{addr}'
       where
           e_id='{e_id}'
        '''
cnt = cur.execute(query)

# print("cnt",cur.rowcount) # 성공시 1
print("cnt",cnt) # 성공시 1

con.commit()

cur.close()
con.close()
    
        
