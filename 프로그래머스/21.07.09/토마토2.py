import collections, sys

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
check = [[[0]*m for _ in range(n)] for _ in range(h)]



queue = collections.deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1 and check[z][x][y] == 0:
                queue.append((z,x,y))
                check[z][x][y] = 1


def bfs():
    dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
    
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0 and check[nz][nx][ny] == 0:
                    check[nz][nx][ny] = check[z][x][y] + 1
                    graph[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))


bfs()
checker = True

for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            checker = False
            sys.exit()
curMax = 0

for i in check:
    for j in i:
        list_max = max(j)
        curMax = max(curMax, list_max)

#if checker:
print(curMax-1)
