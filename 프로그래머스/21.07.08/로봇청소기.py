import collections
from sys import getrecursionlimit


def bfs(x, y):
    queue = collections.deque()
    queue.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'x':
                    continue
                if graph[nx][ny] == '.' and check[nx][ny] == 0:
                    check[nx][ny] = check[x][y] + 1
                    queue.append((nx,ny))
                elif graph[nx][ny] == '*':
                    graph[nx][ny] = '.'
                    check[nx][ny] = check[x][y] + 1
                        

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [list(input()) for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    # print('---------------')
    # print(graph)
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 'o':
                bfs(x,y)
    # print(graph)
    # print('---------------')
    checker = True
    for i in graph:
        if '*' in i:
            checker = False
            print(-1)
            break
    curMax = 0
    for i in check:
        curMax = max(curMax, max(i))
    if checker:
        print(curMax)
        
