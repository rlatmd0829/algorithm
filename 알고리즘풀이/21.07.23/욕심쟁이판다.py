import collections
import sys

input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
#visited = [[False for _ in range(n)] for _ in range(n)]
#distance = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0 ,-1, 1]
queue = collections.deque()
maxx = 0
def bfs(x,y):
    global maxx
    distance[x][y] = 1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > graph[x][y] and distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    maxx = max(maxx, distance[nx][ny])
                    queue.append((nx,ny))
    return maxx
maxCur = 0
for i in range(n):
    for j in range(n):
        #visited = [[False for _ in range(n)] for _ in range(n)]
        distance = [[0 for _ in range(n)] for _ in range(n)]
        maxx = bfs(i,j)
        maxCur = max(maxCur, maxx)
        # for k in range(n):
        #    maxCur = max(maxCur, max(distance[k]))
print(maxx)