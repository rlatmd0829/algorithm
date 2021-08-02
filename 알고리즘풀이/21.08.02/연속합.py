n = int(input())
link = list(map(int, input().split()))


for i in range(1, n):
    link[i] = max(link[i], link[i] + link[i-1])

print(max(link))