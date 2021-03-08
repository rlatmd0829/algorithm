import math
a,b = map(int,input().split())

for i in range(a,b+1):
    if(i==1):
        continue
    n=int(math.sqrt(i))
    for j in range(2,n+1):
        if i%j == 0:
            break
    else:
        print(i)

