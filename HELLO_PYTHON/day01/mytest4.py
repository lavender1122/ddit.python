#출력할 단수를 입력하세요 ex) 4

a = input("첫수 입력하시오")

arr = list(range(1,9+1))
avg = 0

for i in arr:
    avg=int(a) *i
    print(a,"*",i,"=",avg)


#파이썬 여러줄 주석 처리 : ctrl + /
#이중 for 문
# arr2 = list(range(2,9+1))
# for i in arr:
#     for j in arr2:
#         avg = i*j
#         print(i,"*",j,"=",avg)
    