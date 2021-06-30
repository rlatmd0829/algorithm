from itertools import combinations
n = int(input())
demo = [i+1 for i in range(n)]

a = [list(map(int,input().split())) for _ in range(n)]
arr = list(combinations(demo,len(demo)//2))

# 1 3 6, 2 4 5
# 3+2 = 5, 7, 9
# 7, 10, 8

for i in arr:
    for j in range(len(i)-1):
        answer = answer + a[i[j]][i[j+1]] + a[i[j+1]][i[j]]