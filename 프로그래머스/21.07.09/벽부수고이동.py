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

##################

from sys import stdin
from collections import deque

N,M = map(int, stdin.readline().split(" "))
map = [list(map(int, stdin.readline().strip())) for _ in range(N)]

# 좌표계산 위한 배열
dx = [-1,1,0,0]
dy = [0,0,1,-1]
curMin = 1000000
def bfs():
    global curMin
    # 최단경로 저장 배열. 아직 방문 안했다는 표시는 -1로 
    distances = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    # 큐
    queue = deque()
    queue.append((0,0,0))
    distances[0][0][0] = 1
    while queue:
        x, y, broken = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny <M:
                # 부수지 않고 갈 수 있는 경우
                if map[nx][ny] == 0 and distances[nx][ny][broken] == -1:
                    distances[nx][ny][broken] = distances[x][y][broken]+1
                    queue.append((nx,ny,broken))
                # 부숴야만 갈 수 있는 경우
                    # 지금까지 한번도 안 부쉈어야 한다
                    # 벽이 있어야 한다
                    # 방문기록이 없어야 한다
                elif broken == 0 and map[nx][ny] == 1 and distances[nx][ny][1] == -1:
                    distances[nx][ny][1] = distances[x][y][0]+1
                    queue.append((nx,ny,1))

    if distances[N-1][M-1][0] != -1:
        curMin = min(curMin, distances[N-1][M-1][0])
    if distances[N-1][M-1][1] != -1:
        curMin = min(curMin, distances[N-1][M-1][1])


bfs()

if curMin == 1000000:
    print(-1)
else:
    print(curMin)