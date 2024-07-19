import pymysql
con = pymysql.connect(host='localhost', user='root', port=3305
                       ,password='python', db='python', charset='utf8')
# cur = con.cursor(pymysql.cursors.DictCursor)
cur = con.cursor(pymysql.cursors.DictCursor)

sql = f'''
        SELECT
            e_id,
            e_name,
            gen,
            addr
        FROM emp
    '''
cur.execute(sql)

result = cur.fetchall()
print(result)

cur.close()
con.close()
