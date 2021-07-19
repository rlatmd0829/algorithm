n = int(input())

graph = [[] for _ in range(n+1)]

cost = [0]+list(map(int, input().split()))
visited = [0 for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]


for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = 1
    dp[cur][1] = cost[cur] # 현재마을을 우수마을로 포함했으니까 현재마을에 cost를 더해준다.
    for next in graph[cur]:
        if not visited[next]:
            dfs(next)
            dp[cur][1] += dp[next][0] # 현재마을을 우수마을로 선정하면 다음마을은 우수마을일수 없다.
            dp[cur][0] += max(dp[next][0], dp[next][1]) # 현재 마을을 우수마을로 선정 x
dfs(1)
print(max(dp[1][1], dp[1][0]))