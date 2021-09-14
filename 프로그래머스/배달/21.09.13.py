import sys
import heapq
def solution(N, road, K):
    answer = 0
    INF = sys.maxsize
    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]
    
    for a,b,c in road:
        graph[a].append((c,b))
        graph[b].append((c,a))
    
    
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    def dijkstra():
        while queue:
            wei, now = heapq.heappop(queue)
            if distance[now] < wei:
                continue
            for w, next in graph[now]:
                next_w = w + wei
                if distance[next] > next_w:
                    distance[next] = next_w
                    heapq.heappush(queue, (next_w, next))
    dijkstra()
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer