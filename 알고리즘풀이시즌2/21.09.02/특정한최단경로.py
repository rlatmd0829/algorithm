import heapq
import sys
n , e = map(int, input().split())
input = sys.stdin.readline
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
answer1 = 0
answer2 = 0

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

o, p = map(int, input().split())

queue = []

def dijstra(index):
    distance = [INF for _ in range(n+1)]
    distance[index] = 0
    heapq.heappush(queue, (0, index))
    while queue:
        wei, cur = heapq.heappop(queue)
        if distance[cur] < wei:
                continue
        for w, next in graph[cur]:
            next_wei = w + wei
            if next_wei < distance[next]:
                distance[next] = next_wei
                heapq.heappush(queue, (next_wei, next))
    return distance

distance = dijstra(1)
answer1 += distance[o]
distance = dijstra(o)
answer1 += distance[p]
distance = dijstra(p)
answer1 += distance[n]


distance = dijstra(1)
answer2 += distance[p]
distance = dijstra(p)
answer2 += distance[o]
distance = dijstra(o)
answer2 += distance[n]

if answer1 >= INF and answer2 >= INF:
    print(-1)
else:
    print(min(answer1, answer2))
            

