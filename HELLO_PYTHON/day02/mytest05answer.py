from random import random
# 홀/짝을 입력하시오 홀
# 나: 홀
# 컴 : 짝
# 결과 : 짐

mine = ""
com = ""
result = ""

mine - input("가위바위보")

rnd = random()

if rnd > 0.66:
    com ="가위"
elif rnd > 0.33:
    com = "바위"
else:
    com = "보"
    
if mine == "가위" and com == "가위": result ="비김"
if mine == "가위" and com == "바위": result ="짐"
if mine == "가위" and com == "보": result ="이김"

if mine == "바위" and com == "보": result ="이김"
if mine == "바위" and com == "보": result ="이김"
if mine == "바위" and com == "보": result ="이김"