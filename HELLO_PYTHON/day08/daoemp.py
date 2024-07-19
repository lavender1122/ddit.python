import pymysql
class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', port=3305
                       ,password='python', db='python', charset='utf8')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = f'''
            SELECT
                e_id,
                e_name,
                gen,
                addr
            FROM emp
            '''
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    def select(self,e_id):
        sql = f'''
            SELECT
                e_id,
                e_name,
                gen,
                addr
            FROM emp
            where
            e_id= '{e_id}'
            '''
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f'''
           Insert into emp(e_id,e_name,gen,addr)
           values('{e_id}','{e_name}','{gen}','{addr}')
        '''
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
        
    def update(self,e_id,e_name,gen,addr):
        sql = f'''
           update emp
           set
               e_name='{e_name}',
               gen='{gen}',
               addr='{addr}'
           where
               e_id='{e_id}'
            '''
        
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f'''
           delete from emp 
           where
           e_id='{e_id}'
        '''
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
        
    def __del__(self):
        self.cur.close()
        self.con.close()
    
        
if __name__ == '__main__':
    de= DaoEmp()
    # vo = de.select(1)
    # cnt = de.delete(3)
    # print("cnt",cnt)
    # print("vo",vo)       
    
    
