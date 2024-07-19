import pymysql
class DaoStock:
    def __init__(self):
            # MySQL 연결
            self.con = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                           db='python', charset='utf8')
                           
            # Cursor 생성
            self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    def insert(self, s_code, s_name, price, ymd):    
        query = f"""
        INSERT INTO stock
        VALUES("{s_code}", "{s_name}", {s_price}, "{ymd}")
        """
        cnt =self.cur.execute(query)
        self.con.commit()
        return cnt
        
if __name__ == '__main__':
    de = DaoStock()
    # de.insert(1, 1, 1, 1)
