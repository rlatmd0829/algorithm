from itertools import permutations

n = int(input())
demo = list(map(int,input().split()))
curMax = 0
per = list(permutations(demo))
for i in per:
    answer = 0
    for j in range(n-1):
        answer += abs(i[j] - i[j+1])
    curMax = max(curMax, answer)

print(curMax)
