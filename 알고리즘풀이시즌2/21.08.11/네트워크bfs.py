# bfs로 못풀음
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
queue = []

for i in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((w,y))
    graph[y].append((w,x))
    heapq.heappush(queue, (w, x))



def bfs(start):
    heapq.heappush(queue, (0, start))
    while queue:
        w,cur = heapq.heappop(queue)
        
        visited[cur] = True
        for wei,next in graph[cur]:
            
            if visited[next] == False:
                print(cur, next)
                visited[next] = True
                distance[next] = distance[cur] + wei
                heapq.heappush(queue, (wei, next))
bfs(2)
print(distance)