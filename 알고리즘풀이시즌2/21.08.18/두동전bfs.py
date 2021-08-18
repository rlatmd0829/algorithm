import collections
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue = collections.deque()

def bfs(x1,y1,x2,y2):
    queue.append((x1,y1,x2,y2,0))
    while queue:
        x1,y1,x2,y2,cnt = queue.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if graph[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if graph[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                queue.append((nx1,ny1,nx2,ny2,cnt+1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
            else:
                continue
    return -1
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            result.append((i,j))

print(bfs(result[0][0], result[0][1], result[1][0], result[1][1]))