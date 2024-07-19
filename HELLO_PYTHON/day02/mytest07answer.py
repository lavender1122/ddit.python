#com = (1~99까지를 넣어줘야돼요)
#수를 입력하시오 40
# 40 UP
#수를 입력하시오 60
# 60 DW
# 수를 입력하시오 50
#50 ANSWER
from random import random

com = int(random()*99)+1
print("com ",com)

while True:
    mine = input("수를 입력하시오")
    imine = int(mine)
    if imine > com:
        print("{}\tDW".format(imine))
    elif imine < com:
        print("{}\tUP".format(imine))
    else:
        print("{}\tANSWER".format(imine))
        break
        
        
