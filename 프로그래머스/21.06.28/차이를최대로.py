from itertools import permutations
n = int(input())

a = list(map(int, input().split()))
b = list(permutations(a))
ans = 0
for i in b:
    sums = 0
    for j in range(n-1):
        sums += abs(i[j]-i[j+1])
    ans = max(ans, sums)
print(ans)