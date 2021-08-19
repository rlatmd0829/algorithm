import collections
n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
S,X,Y = map(int, input().split())
queue = collections.deque()

def bfs():
    while queue:
        time,x,y = queue.popleft()
        if time == S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y]
                    queue.append((time+1,nx,ny))
        
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            result.append([graph[i][j],0,i,j])

result.sort()


for value,time,i,j in result:
    queue.append((time,i,j))

bfs()
print(graph[X-1][Y-1])

