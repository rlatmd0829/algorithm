n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

counts = [0] * 100000
counts[0] = 1

for coin in coins:
    for price in range(10001):
        if price >= coin:
            counts[price] += counts[price-coin]

print(counts[k])

# 동전1 : k원이 되는 동전의 경우의 수 => 모든 경우의 수를 다더하는 느낌, 경우의 수 이므로 counts[0] = 1 이고 경우의 수끼리 더해 나간다.
# dp[k] = dp[k] + dp[k-coin]
# 1, 2, 5 코인이라면 
# dp[10] = dp[10] + dp[10-1]
# dp[10] = dp[10] + dp[10-2]
# dp[10] = dp[10] + dp[10-5]

# 동전2 : k원이 되는 동전의 최소 갯수 => 동전 사용 최소 갯수를 찾기위해 counts[0] = 0이고 +1로만 증가한다.
# dp[k]의 최소 갯수를 구하려면 min(dp[k-coin]) + 1 을 하면 된다.
# 1, 5, 12의 코인이 있다면 dp[15] = min(dp[15-1], dp[15-5], dp[15-12]) + 1 이다