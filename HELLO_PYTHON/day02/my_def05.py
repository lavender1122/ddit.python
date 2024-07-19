# def => function
#스크립트 언어라서 위->아래 읽어서 아래에 위치하면 안됨
def add_min_mul_div(a,b):
    return a+b, a-b,a*b,a/b

sum= add_min_mul_div(4,2) 
#sum:(6, 2, 8, 2.0) => 작은 괄호 라서 작은 배열이라고 생각하면됨
print("sum:{}".format(sum))
print(sum[2]) #tuple
 

