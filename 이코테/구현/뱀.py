import collections
n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    x,y = map(int, input().split())
    graph[x][y] = 2

l = int(input())
direction = []
for i in range(l):
    x,y = input().split()
    direction.append([int(x),y])

direction.sort()

dx,dy = [0,1,0,-1],[1,0,-1,0] # 우하좌상

def simulation(x,y):
    d = 0 # 방향
    graph[x][y] = 1
    queue = collections.deque()
    queue.append((x,y))
    time = 0
    
    while queue:
        
        time += 1
        x += dx[d]
        y += dy[d]
        if 1 <= x < n+1 and 1 <= y < n+1 and graph[x][y] != 1:
            if graph[x][y] == 2:
                graph[x][y] = 1
            elif graph[x][y] == 0:
                nx,ny = queue.popleft() # 꼬리에 위치
                graph[x][y] = 1
                graph[nx][ny] = 0
            queue.append((x,y))
        else:
            return time
        
        if direction:
            if time == int(direction[0][0]):
                if direction[0][1] == 'D':
                    d = (d+1) % 4
                else:
                    d = (d-1) % 4
                direction.pop(0)
print(simulation(1,1))




