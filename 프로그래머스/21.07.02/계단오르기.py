import sys
input = sys.stdin.readline

n = int(input())
dp = []
stairs = [int(input()) for _ in range(n)]

dp.append(stairs[0])
dp.append(max(stairs[0]+stairs[1], stairs[1]))
dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, n):
    dp.append(max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i]))

print(dp.pop())


