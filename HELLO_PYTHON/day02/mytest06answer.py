#첫수를 입력하세요 1
# 끝 수를 입력하시오 5
# 배수를 입력하세요 2
# 1에서 5까지의 2의 배수의 합은 6입니다.

a=input("첫수를 입력하세요")
b=input("끝 수를 입력하세요")
c=input("배수를 입력하세요")

aa=int(a)
bb=int(b)
cc=int(c)

sum=0
for i in range(aa,bb+1):
    if i%cc ==0:
        sum += i


print("{}에서 {} 까지의 {}의 배수의 합은 {} 입니다.". format(a,b,c,sum))
