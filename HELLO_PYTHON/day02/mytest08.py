#첫별수를 입력하세요 3
#끝 별수를 입력하세요 5
#🧡🧡🧡🧡
#🧡🧡🧡🧡🧡

aa=input("첫별수를 입력하세요")
bb=input("끝 별수를 입력하세요")
a = int(aa)
b = int(bb)

arr= list(range(a,b+1))
print(arr)

for i in arr:
    print("집가고싶다"*i)
