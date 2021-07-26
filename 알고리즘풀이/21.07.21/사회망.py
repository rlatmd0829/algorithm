import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
for i in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = True
    dp[cur][1] = 1
    for next in graph[cur]:
        if visited[next] == False:
            dfs(next)
            # dp의 값은 최소개수를 나타낸다. 예를들어 dp[1][0]이라면 1번이 얼리어답터가 아닐때 1번까지의 얼리어답터의 최소 개수이다.
            # dfs 재귀 부터 시작하고 값을 더하므로 루트노드에 값이 쌓이게 된다.
            dp[cur][0] += dp[next][1] # 현재 노드가 얼리어답터가 아닌경우 인접노드는 얼리어답터이다.
            dp[cur][1] += min(dp[next][0], dp[next][1]) # 현재 노드가 얼리어답터인 경우는 인접노드가 얼리어답터 일수 있고 아닐 수 있다. 그중 최솟값

dfs(1)
print(dp)
print(min(dp[1][0], dp[1][1]))