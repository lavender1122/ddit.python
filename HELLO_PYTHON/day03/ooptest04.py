class Mavely:
    def __init__(self):
        self.weight = 100
    def eat(self,amount):
        self.weight += amount
if __name__ == '__main__':
    ma = Mavely()
    print("ma.weight :",ma.weight)
    ma.eat(5)
    print("ma.eat :",ma.weight)
    