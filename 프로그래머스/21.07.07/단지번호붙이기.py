n = int(input())

graph = [list(map(int,input())) for _ in range(n)]

check = [[False]*n for _ in range(n)]

def bfs(x,y):
    danji = 0
    queue = []
    queue.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and check[nx][ny] == False:
                    danji += 1
                    check[nx][ny] = True
                    queue.append((nx,ny))
    return danji

count = 0
result = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and check[x][y] == False:
            result.append(bfs(x,y))
            count += 1
print(count)
result.sort()
for i in result:
    print(i)
