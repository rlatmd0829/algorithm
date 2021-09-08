n = int(input())

value = [int(input()) for _ in range(n)]

dp = [0] * n
if n == 1:
    print(value[0])
elif n == 2:
    print(value[0] + value[1])
else:
    dp[0] = value[0]
    dp[1] = value[0] + value[1]
    dp[2] = max(value[1] + value[2], value[0] + value[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + value[i], dp[i-3] + value[i-1] + value[i], dp[i-1])

    print(max(dp))