n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort()

counts = [10001] * (k+1)
counts[0] = 0

for coin in coins:
    for price in range(coin, k+1):
        counts[price] = min(counts[price], counts[price-coin] + 1)

if counts[k] == 10001:
    print(-1)
else:
    print(counts[k])