# 다익스트라로 못풀음
import heapq
import sys

n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for i in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((w,y))
    graph[y].append((w,x))


def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        wei, now = heapq.heappop(queue)
        if distance[now] < wei:
            continue
        for w, next_node in graph[now]:
            next_w = wei + w
            if distance[next_node] > next_w:
                distance[next_node] = next_w
                heapq.heappush(queue, (next_w, next_node))
dijkstra(1)
print(distance)
print(max(distance))