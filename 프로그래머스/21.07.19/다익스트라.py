import sys
import heapq

V, E = map(int, input().split())

K = int(input())

INF = sys.maxsize
graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v)) # 힙을 만들때 가중치로 힙이 정렬을 하기 위해서 가중치를 앞에 쓴다.

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if distance[now] < wei:
            continue

        for w, next_node in graph[now]:
            # 현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node) 까지의 가중치 w
            
            # 다음 노드까지의 가중치 next_wei
            next_wei = w + wei

            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
dijkstra(K)
for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])


