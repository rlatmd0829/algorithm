from itertools import combinations
n, m = map(int,input().split())
a = list(map(int, input().split()))

arr=list(combinations(a,3))

answer = 0
for i in arr:
    sum= 0
    for j in i:
        sum += j
    if sum <= m:
        answer = max(answer, sum)
print(answer)
