from itertools import combinations
import sys
INF = sys.maxsize
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            home.append((x,y))
        if graph[x][y] == 2:
            chicken.append((x,y))

pick_chicken = list(combinations(chicken,m))
result = [0] * len(pick_chicken)

for i in home:
    for j in range(len(pick_chicken)):
        minn = INF
        for k in pick_chicken[j]:
            temp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            minn = min(minn, temp)
        result[j] += minn
print(min(result))

