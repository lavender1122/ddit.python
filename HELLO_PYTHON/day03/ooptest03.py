class Wonbin:
    def __init__(self):
        self.flag_ugly = True
    def plastic(self):
        self.flag_ugly = False

#메인
if __name__ == '__main__':
    #객체 생성
    won = Wonbin()
    #생성된 객체 필드 가져오기
    print("Wonbin",won.flag_ugly)
    #클래스 안에 있는 메서드 가져오기
    won.plastic()
    print("Wonbin",won.flag_ugly)
    