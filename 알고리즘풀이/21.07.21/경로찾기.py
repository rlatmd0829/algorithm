import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
demo = [list(map(int,input().split())) for _ in range(n)]
graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if demo[i][j] == 1:
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ') # 길이없는경우 INF일 경우에만 0을 출력
        else:
            print(1, end=' ') # 자기자신에게 가는것도 길이 있는것이므로 1이 출력된다.
    print()