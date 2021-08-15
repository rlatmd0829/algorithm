# 유레카이론 부터
from itertools import combinations
t = int(input())

for i in range(t):
    n = int(input())
    ure = []
    for j in range(1,n+1):
        ure.append(j*(j+1)/2)
    com = list(combinations(ure, 3))
    
    for j in com:
        if sum(j) == n:
            print(1)
            break
    else:
        print(0)


    