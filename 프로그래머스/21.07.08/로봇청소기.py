import collections
from sys import getrecursionlimit


def bfs(x, y):
    queue = collections.deque()
    queue.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    time = -1
    while queue:
        time += 1
        for i in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 'x':
                        continue
                    if graph[nx][ny] == '.' and check[nx][ny] == False:
                        check[nx][ny] = True
                        queue.append((nx,ny))
                    elif graph[nx][ny] == '*':
                        graph[nx][ny] = '.'
                        check[nx][ny] = True
                        
    return time

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [list(input()) for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    # print('---------------')
    # print(graph)
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 'o':
                time = bfs(x,y)
    # print(graph)
    # print('---------------')
    checker = True
    for i in graph:
        if '*' in i:
            checker = False
            print(-1)
            break
    if checker:
        print(time)
