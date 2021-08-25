# dfs 사용하여 사이클 찾기 문제 어렵다.

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
check = False
def dfs(x,y,cnt,Dx,Dy):
    global check
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if check: # 사이클이 한개라도 존재하면 더 돌필요없다.
            return

        if 0 <= nx < n and 0 <= ny < m:
            if cnt >= 4:
                if Dx == nx and Dy == ny:
                    check = True
                    return

            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx,ny,cnt+1,Dx,Dy)
                #visited[nx][ny] = False # visited 초기화를 하기 때문에 필요없는거 같다..?
    return

for x in range(n):
    for y in range(m):
        if visited[x][y] == False:
            visited = [[False]*m for _ in range(n)] # visited 초기화
            Dx, Dy = x,y
            visited[Dx][Dy] = True
            dfs(x,y,1,Dx,Dy) # 자기 자신 포함 cnt 1부터
            
            if check:
                print("Yes")
                sys.exit()
print("No")