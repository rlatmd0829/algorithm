import collections
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

def bfs():
    time = -1
    queue = collections.deque()
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                queue.append((x,y))
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        time += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0 and check[nx][ny] == -1:
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
    return time

time = bfs()
checker = True
for i in graph:
    if 0 in i:
        checker = False
        print(-1)
        break

if checker:
    print(time)