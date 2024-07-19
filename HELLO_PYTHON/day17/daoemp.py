import pymysql
class DaoBlog:
    def __init__(self):
            # MySQL 연결
            self.con = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                           db='python', charset='utf8')
                           
            # Cursor 생성
            self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    def insert(self, title, link, description, bloggername, bloggerlink, postdate):    
        query = f"""
        INSERT INTO blog (title, link, description, bloggername, bloggerlink, postdate) 
        VALUES("{title}", "{link}", "{description}", "{bloggername}", "{bloggerlink}", "{postdate}")
        """
        cnt =self.cur.execute(query)
        self.con.commit()
        return cnt
        
if __name__ == '__main__':
    de = DaoBlog()
