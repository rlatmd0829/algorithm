import collections
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
distance = [0 for _ in range(N+1)]

for i in range(M):
    x,y = map(int, input().split())
    graph[x].append(y)

queue = collections.deque()
queue.append(X)
def bfs():
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                distance[next] = distance[cur] + 1
                queue.append(next)

bfs()
print(distance)
result = []
for i in range(1, len(distance)):
    if distance[i] == K:
        result.append(i)
result.sort()
if result:
    for i in result:
        print(i)
else:
    print(-1)


