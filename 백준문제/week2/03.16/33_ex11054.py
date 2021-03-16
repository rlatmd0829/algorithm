N = int(input())
lst = list(map(int, input().strip().split()))

dp = [0 for i in range(N)]
dp2 = [0 for i in range(N)]


# 정방향으로 LIS를 찾는다.
for i in range(N):
    for j in range(i):
        if (lst[i] > lst[j] and dp[i] < dp[j]): # lst[i]보다 작은 값이면서 가장 긴 수열에 길이를 받아서 dp[i]에 넣는다.
            dp[i] = dp[j]
    dp[i] += 1

# 역방향으로 LIS를 찾는다.
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if (lst[i] > lst[j] and dp2[i] < dp[j]):
            dp2[i] = dp2[j]
    dp2[i] += 1


MAX = 0
for i in range(N):
    if dp[i]+dp2[i] > MAX:
        MAX = dp[i] + dp2[i]
print(MAX-1) # dp[i] 는 앞에서 부터 i까지 수열의 길이이고 dp2[i]는 뒤에서부터 i까지 길이이다. i가 2번 더해지니까 -1을 해준다.