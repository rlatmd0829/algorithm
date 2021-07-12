n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

counts = [0] * 100000
counts[0] = 1

for coin in coins:
    for price in range(10001):
        if price >= coin:
            counts[price] += counts[price-coin]

print(counts[k])

