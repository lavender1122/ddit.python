#첫수를 입력하시오 ex) 1
#끝수를 입력하시오 ex) 4
#1 에서 4까지 합은 10 입니다.

a = input("첫수 입력하시오")
print("a",a)

b = input("끝 수 입력하시오")
print("b",b)

arr= list(range(int(a),int(b)+1))
sum = 0

for i in arr:
    sum += i;
   
print("1에서 4까지 합은",sum, "입니다.");
