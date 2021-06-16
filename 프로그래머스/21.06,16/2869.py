a, b, v = map(int,input().split())
answer = 0
count = 0
for i in range(1000000000):
    if a*i - b*(i-1) >= v:
        break
print(i)