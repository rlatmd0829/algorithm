from itertools import combinations
n, s = map(int,input().split())

demo = list(map(int, input().split()))
result = []
for i in range(1,len(demo)+1):
    result.extend(list(combinations(demo, i)))

count = 0
for i in result:
    if sum(i) == s:
        count += 1
print(count)