#첫별수를 입력하세요 3
#끝 별수를 입력하세요 5
#🧡🧡🧡🧡
#🧡🧡🧡🧡🧡

def getStar(cnt):
    ret = ""
    for i in range(cnt):
        ret += "*"
    return ret

f = input("첫별수를 입력하시오")
l = input("끝별수를 입력하시오")

ff = int (f)
ll = int (l)

for i in range(ff,ll +1):
        print(getStar(i))

