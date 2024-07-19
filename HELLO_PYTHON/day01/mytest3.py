#첫 수를 입력하시오 ex) 5
#둘째 수를 입력하시오 ex) 5
#5는 6보다 작습니다.
#5는 5는 같은 수입니다.
#7는 5보다 큽니다.

a = input("첫수 입력하시오")
aa=int(a)

b = input("끝 수 입력하시오")
print("b",b)
bb = int(b)
if aa > bb:
    print(a ,"는",b,"보다 큽니다.")
elif aa == bb:
    print(a ,"는",b,"는 같은 수입니다.")
elif aa < bb:
    print(a ,"는",b,"는 작습니다.")