#첫수를 입력하세요 1
# 끝 수를 입력하시오 5
# 배수를 입력하세요 2
# 1에서 5까지의 2의 배수의 합은 6입니다.

aa=input("첫수를 입력하세요")
a=int(aa)
bb=input("끝 수를 입력하세요")
b= int(bb)
cc=input("배수를 입력하세요")
c = int(cc)
sum = 0

arr= list(range(a,b+1))

for i in arr:
    f=arr[i-1]
    if f%c ==0:
        sum=sum+f

print(a,"에서 ",b,"까지의",c,"의 배수의 합은",sum,"입니다.")


