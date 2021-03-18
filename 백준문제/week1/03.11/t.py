
N, K = map(int, input().split())
node= list(map(int, input().split()))
node.sort()
Sum = len(node)
cnt = 0
while True:
    if Sum <= 0:
        break
    Sum = Sum - K + 1
    cnt += 1

print(cnt)