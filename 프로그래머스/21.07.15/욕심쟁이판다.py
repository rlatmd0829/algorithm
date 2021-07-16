from sys import setrecursionlimit 
setrecursionlimit(10**9)


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

distance = [[-1] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x,y):
    if distance[x][y] < 0:
        distance[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[x][y] < graph[nx][ny]:
                    distance[x][y] = max(distance[x][y], dfs(nx,ny)) # x,y에 주변을 검사해 가장 큰값에 +1을 해주면 현재 좌표에 가장 큰 값이 들어가게 된다.
        distance[x][y] += 1
    
    return distance[x][y]

ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, dfs(x,y))
print(ans)

#############################

# n = int(input())

# graph = [list(map(int, input().split())) for _ in range(n)]

# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# def dfs(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if graph[x][y] < graph[nx][ny] and distance[nx][ny] == 1:
#                 distance[nx][ny] = distance[x][y] + 1
#                 distance[nx][ny] = max(distance[nx][ny], dfs(nx,ny))
#     curMax = 0
#     for i in distance:
#         curMax = max(curMax, max(i))
#     return curMax

# ans = 0
# for x in range(n):
#     for y in range(n):
#         distance = [[1] * n for _ in range(n)]
#         ans = max(ans, dfs(x,y))

# print(ans)