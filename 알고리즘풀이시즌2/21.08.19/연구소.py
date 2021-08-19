import collections
import sys

input = sys.stdin.readline
n,m = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
maxx = 0
queue = collections.deque()
dx,dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    global maxx
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visited[i][j] == False:
                count += 1
    
    maxx = max(maxx, count)

def recursive(index):

    if index == 3:
        bfs()
        return 

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                recursive(index+1)
                graph[i][j] = 0

recursive(0)
print(maxx)