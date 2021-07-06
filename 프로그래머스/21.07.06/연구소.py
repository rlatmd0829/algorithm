import collections, sys
n, m = map(int, input().split())

# 벽을 세우고 bfs를 돌리고 queue에는 바이러스인 2를 다 넣어줘서 퍼지게 만들어주고
# 마지막으로 0인 값은 안전영역이기 때문에 0인 갯수를 세어주면 된다.

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


curMax = 0


def bfs():
    global curMax

    check = [[-1] * m for _ in range(n)]
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    queue = collections.deque()

    # 바이러스를 모두 돌아주기 위해서 큐에 모든 바이러스를 넣어줌
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
                check[i][j] = 0

    while queue: 
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 퍼질수 있는곳 이고(0인곳), 한번도 바이러스가 방문하지 않은 곳이면, 큐에 담는다.
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and check[nx][ny] == -1:
                    queue.append((nx,ny))
                    check[nx][ny] = 0
    
    # 바이러스가 다 퍼진 다음에 안전영역을 체크하여 count를 세준다.
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0 and check[x][y] == -1:
                count += 1
    
    curMax = max(curMax, count)

# 3개의 벽을 세우는 모든 경우의 수
def recursive(index):

    # 탈출조건
    if index == 3:
        bfs()
        return
    
    for x in range(n):
        for y in range(m):
            # 일반구역이라면, 벽을 세워서 다음으로 넘긴다.
            if graph[x][y] == 0:
                graph[x][y] = 1
                recursive(index+1)
                # 재귀가 끝나면 최대로 3개의 벽을 세울수 있어서 다른곳도 세워보기 위해서 벽을 허문다. (0으로 만들어준다.) 이 부분 어떻게 동작하는지는 살짝 이해안감
                graph[x][y] = 0

recursive(0)
print(curMax)