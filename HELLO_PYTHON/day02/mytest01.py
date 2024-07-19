from random import random
# 홀/짝을 입력하시오 홀
# 나: 홀
# 컴 : 짝
# 결과 : 짐

# a = input("홀/짝을 입력하시오")
# print("나 : ", a)
# b=random()
# print(b)

# if a =="홀":
#     print()


# if b <0.5:
#     b="홀"
#     print("컴", b)
#     if a =="홀":
#         print("결과 : 이김")
#     else:
#         print("결과 : 짐")
# else:
#     b="짝"
#     print("컴 :", b)
#     if a =="홀":
#         print("결과: 짐")
#     else:
#         print("결과 : 이김")

#쌤 로직
#선언부
mine = ""
com = ""
result = ""

mine = input("홀/짝을 입력하시오")

#비지니스 로직
rnd=random()
if rnd > 0.5:
    com = "홀"
else:
    com = "짝"
    
if mine == com:
    result = "이김"
else:
     result = "짐"
    
print("나 : {}".format(mine))
print("컴 : {}".format(com))
print("결과 : {}".format(result))