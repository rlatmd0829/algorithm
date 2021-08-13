import collections
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [-1,1,0,0],[0,0,-1,1]
queue = collections.deque()
def bfs(a,b):
    queue.append((a,b))
    size = 2
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if graph[nx][ny] < size:
                    graph[x][y] = 0
                    graph[nx][ny] = 9
