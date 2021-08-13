x,y = list(input().split())

result = []
for i in range(len(y) - len(x) +1):
    cnt = 0
    for j in range(len(x)):
        if x[j] != y[j+i]:
            cnt += 1
    result.append(cnt)
print(min(result))