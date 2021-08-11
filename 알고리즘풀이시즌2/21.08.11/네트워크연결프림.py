# 최소스패닝 트리문제(정답)
import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((w,y))
    graph[y].append((w,x))

queue = []

def Prim(start):
    answer = 0
    heapq.heappush(queue, (0, start))
    while queue:
        wei, now = heapq.heappop(queue)
        
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for w, next in graph[now]:
                heapq.heappush(queue, (w, next))
    return answer

print(Prim(1))
