n = int(input())

values = [list(input().split()) for _ in range(n)]

values.sort(key = lambda x : (-int(x[1]), x[2], -int(x[3]), x[0]))
print(values)
for value in values:
    print(value[0])
