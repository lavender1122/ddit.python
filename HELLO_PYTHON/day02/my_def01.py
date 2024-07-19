# def => function
#스크립트 언어라서 위->아래 읽어서 아래에 위치하면 안됨
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
sum = add(4,2)
# print("sum"+sum) => 에러can only concatenat ~~
print("sum",sum)
#format 숫자 문자 상관없이 {}넣어줌
print("sum:{}".format(sum)) 

min = minus(4,2)
print("min",min)

mul = multiply(4,2)
print("mul:",mul)

div= divide(4,2)
print("div:{}".format(div))