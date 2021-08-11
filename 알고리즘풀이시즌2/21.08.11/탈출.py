# 포기
import collections
r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
distance = [[0]*c for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = collections.deque()

def update(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            graph[nx][ny] = '*'

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                elif graph[nx][ny] == '*':
                    if graph[x][y] == '.':
                        graph[x][y] = '*'
                if graph[nx][ny] == 'D':
                    return True
    return False

for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            check = bfs(x,y)
        elif graph[x][y] == 'D':
            answer_x = x
            answer_y = y
if check:
    print(distance[answer_x][answer_y])
else:
    print("KAKTUS")
