n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = 1
    for next in graph[cur]:
        if visited[next] == 0:
            dfs(next)
            visited[cur] += visited[next]
dfs(r)
for i in range(q):
    print(visited[int(input())])
print(visited)
