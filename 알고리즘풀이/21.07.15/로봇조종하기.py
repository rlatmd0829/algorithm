import collections
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

distance = [[0]*m for _ in range(n)]

dx, dy = [1, 0 ,0], [0, -1, 1]

def bfs():
    queue = collections.deque()
    queue.append((0,0))
    distance[0][0] = graph[0][0]
    while queue:
        x,y = queue.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny < m:
                distance[nx][ny] = max(distance[nx][ny], distance[x][y] + graph[nx][ny])
                queue.append((nx,ny))

bfs()
print(distance[n-1][m-1])