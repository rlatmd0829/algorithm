from itertools import combinations
from collections import Counter
import sys

n = int(input())
value = list(map(int, input().split()))
com = []
result = []
for i in range(1,n+1):
    com.extend(list(combinations(value, i)))

for i in com:
    result.append(sum(i))

result = list(set(result))
result.sort()
ret = 1
for i in result:
    if ret != i:
        print(ret)
        sys.exit()
    else:
        ret += 1
print(result[-1] + 1)
