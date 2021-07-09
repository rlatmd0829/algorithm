# 시간초과
import collections

n, m = map(int, input().split())

graph = [list(map(int,input())) for _ in range(n)]


dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    queue = collections.deque()
    queue.append((0,0))
    distance = [[0]*m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))

    return distance[n-1][m-1]


result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            demo = bfs()
            if demo != 0:
                result.append(demo)
            graph[i][j] = 1

if result:
    print(min(result)+1)
else:
    print(-1)

