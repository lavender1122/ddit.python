import pymysql
class DaoQue:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', port=3305
                       ,password='python', db='python', charset='utf8')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    def selectList(self):
        sql = f'''
            SELECT 
            q_num
            ,que
            ,ans1
            ,ans2
            ,ans3
            ,ans4
            ,ans 
            FROM question
            '''
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def select(self,q_num):
        sql = f'''
            SELECT 
            q_num
            ,que
            ,ans1
            ,ans2
            ,ans3
            ,ans4
            ,ans 
            FROM question
            where q_num='{q_num}'
            '''
        self.cur.execute(sql)
        vo  = self.cur.fetchone()
        return vo 
    
    def insert(self,q_num,que,ans1,ans2,ans3,ans4,ans):
        sql = f'''
            INSERT INTO
             question 
             VALUES
             ('{q_num}'
             ,'{que}'
             ,'{ans1}'
             ,'{ans2}'
             ,'{ans3}'
             ,'{ans4}'
             ,'{ans}')
            '''
        cnt=self.cur.execute(sql)
        self.con.commit()
        return cnt 
    
    def update(self,q_num,que,ans1,ans2,ans3,ans4,ans):
        sql = f'''
           UPDATE question SET
            que='{que}'
            ,ans1='{ans1}'
            ,ans2='{ans2}'
            ,ans3='{ans3}'
            ,ans4='{ans4}'
            ,ans='{ans}'
            WHERE
            q_num='{q_num}'
            '''
        cnt=self.cur.execute(sql)
        self.con.commit()
        return cnt 
    
    def delete(self,q_num):
        sql = f'''
            DELETE FROM question
            WHERE
            q_num='{q_num}'
            '''
        cnt=self.cur.execute(sql)
        self.con.commit()
        return cnt 
    
    def __del__(self):
        self.cur.close()
        self.con.close()
        
if __name__ == '__main__':
    dq=DaoQue()
    cnt= dq.delete('3')
    print("cnt",cnt)
    