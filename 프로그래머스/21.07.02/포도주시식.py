n = int(input())
grape = [0] * 10000
for i in range(n):
    grape[i] = int(input())

dp = [0] * 10000
dp[0] = grape[0]
dp[1] = grape[1] + grape[0]
dp[2] = max(grape[2] + grape[0], grape[1] + grape[2], dp[1])

for i in range(3, n):
    dp[i] = max(grape[i] + dp[i-2], grape[i] + grape[i-1] + dp[i-3], dp[i-1])

print(max(dp))