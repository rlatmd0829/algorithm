import collections
import sys
INF = sys.maxsize
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = collections.deque()

def bfs(index):
    queue.append(index)
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                distance[next] = distance[cur] + 1
                queue.append(next)

result = [INF]
for i in range(1,n+1):
    distance = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]   
    bfs(i)
    result.append(sum(distance))

print(result.index(min(result)))

