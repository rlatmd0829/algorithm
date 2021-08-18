import collections
import sys
n, m = map(int, input().split())
minn = sys.maxsize
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = collections.deque()

def bfs(start):
    queue.append(start)
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                distance[next] = distance[cur] + 1
                queue.append(next)

result = []
for i in range(1,n+1):
    distance = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    bfs(i)
    result.append([sum(distance), i])

result.sort()
print(result[0][1])
