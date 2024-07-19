#com = (1~99까지를 넣어줘야돼요)
#수를 입력하시오 40
# 40 UP
#수를 입력하시오 60
# 60 DW
# 수를 입력하시오 50
#50 ANSWER
from random import random

com=int(random()*100);
print(com)
while True:
    aa=input("수를 입력하시오")
    a=int(aa)
    if com==a:
        print(a,"ANSWER")
        break;
    elif com < a:
        print(a, "DW")
    else:
        print(a, "UP")
        
# cnt = 1
# while True:
#     print(cnt,"ch")
#     cnt +=1
#     if cnt>99 :
#         break;
