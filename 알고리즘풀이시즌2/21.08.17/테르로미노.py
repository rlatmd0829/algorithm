import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
visited = [[False]*m for _ in range(n)]
ans = 0
def recursive(x,y,sum,cnt):
    if cnt == 4: # 테트로미노는 4개의 정사각형으로 이루어져있으므로 4곳을 돌면 모두 테트로미노이다.
        global ans
        if ans < sum:
            ans = sum
        return

    if visited[x][y]:
        return

    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            recursive(nx,ny,sum+graph[x][y],cnt+1)
    visited[x][y] = False

for i in range(n):
    for j in range(m):
        recursive(i,j,0,0)
        
        if j+2 < m: # ㅗ 모양은 dx,dy 이동으로 구하기 어려워서 따로 처리한다.
            temp = graph[i][j] + graph[i][j+1] + graph[i][j+2]
            if i-1 >= 0:
                temp2 = temp + graph[i-1][j+1] # ㅗ
                if ans < temp2:
                    ans = temp2
            if i+1 < n:
                temp2 = temp + graph[i+1][j+1] # ㅜ
                if ans < temp2:
                    ans = temp2
        if i+2 < n:
            temp = graph[i][j] + graph[i+1][j] + graph[i+2][j]
            if j+1 < m:
                temp2 = temp + graph[i+1][j+1] # ㅏ
                if ans < temp2:
                    ans = temp2
            if j-1 >= 0:
                temp2 = temp + graph[i+1][j-1] # ㅓ
                if ans < temp2:
                    ans = temp2

print(ans) 

