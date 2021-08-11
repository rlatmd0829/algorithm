n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우 

# 3번 cctv 상우, 상좌, 