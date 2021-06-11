from collections import deque
n, m, v = map(int,input().split())


graph = [[] for _ in range(n+1)]


for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
visited = [False] * (n+1)

for i in range(1, n+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        start = queue.popleft()
        print("strat :" , start)
        print(start, end=' ')
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)
