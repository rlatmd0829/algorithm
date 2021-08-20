import collections
import sys
input = sys.stdin.readline
n,l,r = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [-1,1,0,0], [0,0,-1,1]

queue = collections.deque()
queue.append((0,0))
result = []
def bfs():
    visited = [[False]*n for _ in range(n)]
    ok = False
    for i in range(n):
        for j in range(n):
            
            if visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                answer = graph[i][j]
                s = [(i,j)]
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if l <= abs(graph[nx][ny] - graph[x][y]) <= r and visited[nx][ny] == False:
                                ok = True
                                answer += graph[nx][ny]
                                visited[nx][ny] = True
                                queue.append((nx,ny))
                                s.append((nx,ny))
                val = answer // len(s)
                for x,y in s:
                    graph[x][y] = val
    return ok
ans = 0
while True:
    if bfs():
        ans += 1
    else:
        break
print(ans)