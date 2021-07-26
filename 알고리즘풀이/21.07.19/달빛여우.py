import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for i in range(M):
    a,b,d = map(int, input().split())
    graph[a].append((d,b))
    graph[b].append((d,a))

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)
        if distance[now] < wei:
            continue
        for w, next_node in graph[now]:
            next_wei = wei + w
            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))