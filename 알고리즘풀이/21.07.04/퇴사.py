import sys

n = int(input())

timeTable = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [0 for i in range(n+1)]

for i in range(n-1, -1, -1):
    if i + timeTable[i][0] > n: #일수가 주어진 일수보다 초과된경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1]) # dp[i+1]이랑 dp[i + T값] + 현재 P값

print(dp[0])