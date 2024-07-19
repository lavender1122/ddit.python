import pymysql
con = pymysql.connect(host='localhost', user='root', port=3305
                       ,password='python', db='python', charset='utf8')
# cur = conn.cursor(pymysql.cursors.DictCursor)
cur = con.cursor()
e_id="3"
e_name="3"
gen="3"
addr="3"


query = f'''
       Insert into emp(e_id,e_name,gen,addr)
       values('{e_id}','{e_name}','{gen}','{addr}')
        '''
cnt = cur.execute(query)

# print("cnt",cur.rowcount) # 성공시 1
print("cnt",cnt) # 성공시 1

con.commit()

cur.close()
con.close()
    
        
