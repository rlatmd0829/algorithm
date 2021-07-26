import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = 1
    for next in graph[cur]:
        if visited[next] == 0:
            dfs(next) # dfs를 visited 갱신보다 먼저 한다는 것은 밑으로 쭉 내려가고 올라오면서 값을 쌓아준다는 느낌이다
                        # 그래서 루트노드에 모든 값이 쌓인다.
            visited[cur] += visited[next]
            # 현재 노드에 이동한 노드값을 쌓아주는 거임
#
# if visited[next] == False:
#           distance[next] = distance[cur] + 1 # 이런식으로 이동한 노드값에 값을 쌓아주고 dfs를 돌아주면
#           dfs(next) # 루트노드에 멀어질 수 록 값을 쌓는 느낌

dfs(r)
for i in range(q):
    print(visited[int(input())])

