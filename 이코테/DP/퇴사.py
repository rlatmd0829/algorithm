n = int(input())

value = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if value[i][0] + i > len(value):
        continue
    else:
        dp[i] = value[i][1] + max(dp[i + value[i][0]:])

print(max(dp))