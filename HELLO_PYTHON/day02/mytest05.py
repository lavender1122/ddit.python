#가위/바위/보를 선택하세요 가위
#나 : 가위
#컴 : 보
#결과 : 이김
from random import random
from xml.dom.minidom import AttributeList

mine="가위"
com = ""
result = "" 

# a = input("가위/바위/보를 입력하세요")

if random() <0.33:
   com ="가위" 
elif random()<0.66:
   com ="바위" 
else:
   com ="보" 
   
if(mine=="가위" and com =="보" or mine=="바위" and com == "가위" or mine=="보" and com == "바위"):
     result="이김"
elif(mine=="가위" and com =="가위" or mine=="바위" and com == "바위" or mine=="보" and com == "보"):
    result="비김"
elif(mine=="가위" and com =="바위" or mine=="바위" and com == "보" or mine=="보" and com == "가위"):
    result="컷ㅋㅋㅋ"
    
print("나:",mine,"컴:",com,"결과",result)

