class Animal:
    def __init__(self):
            self.lift_span = 10
    def fightTigher(self):
        self.lift_span =0

class Human(Animal):
    def __init__(self): #생성자
        self.money = 0
        super().__init__()
    def work(self):
        self.money=30000

        
# 파이썬 main
if __name__ == '__main__':
    ani = Animal()
    print("lift_span2",ani.lift_span)
    ani.fightTigher()
    print("lift_span2",ani.lift_span)
    
    h=Human()
    print("h :",h.money)
    h.work()
    print("h work :",h.money)
    h.fightTigher()
    print("lift_span", h.lift_span)
            
