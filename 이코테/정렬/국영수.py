import sys
n = int(input())

input = sys.stdin.readline
values = [list(input().split()) for _ in range(n)]

values.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for value in values:
    print(value[0])
