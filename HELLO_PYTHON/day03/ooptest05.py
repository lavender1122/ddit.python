from day3.ooptest03 import Wonbin
from day3.ooptest04 import Mavely
class YoungHun(Mavely,Wonbin):
    def __init__(self):#생성자
        # super.__init__() #앞에있는 매개변수만 가져옴 ex) Mavely
         Mavely.__init__(self)
         Wonbin.__init__(self)
        
if __name__ == '__main__':
    yh = YoungHun()
    
    print("yh.weight",yh.weight)
    print("yh.flag_ugly",yh.flag_ugly)
    yh.plastic()
    yh.eat(10)
    print("yh.eat",yh.weight)
    print("yh.plastic",yh.flag_ugly)
