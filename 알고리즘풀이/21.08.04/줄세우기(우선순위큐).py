
import heapq
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    distance[y] += 1

queue = []

for i in range(1,n+1):
    if distance[i] == 0:
        heapq.heappush(queue, i)

while queue:
    cur = heapq.heappop(queue)
    print(cur, end = ' ')
    for next in graph[cur]:
        distance[next] -= 1
        if distance[next] == 0:
            heapq.heappush(queue, next)        
