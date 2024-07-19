from random import random
arr = list(range(1,45+1))
#range : 함수형 배열

for i in range(999):
    rnd = int(random()*len(arr))
    a = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a
    
print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])