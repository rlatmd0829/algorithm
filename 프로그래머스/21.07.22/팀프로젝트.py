# 다시풀어보기
import sys
sys.setrecursionlimit(10**6)

t = int(input())

for i in range(t):
    answer = 0
    n = int(input())
    graph = [0]+list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    ans = list()
    
    def dfs(cur):
        global ans
        visited[cur] = True
        loop.append(cur)
        # 무조건 한개씩만 연결되어 있어서 for문을 돌 필요없다.
        num = graph[cur]
        if visited[num]:
            if num in loop:
                ans += loop[loop.index(num):]
            return
        else:
            dfs(num)

    for i in range(1, n+1):
        if visited[i] == False:
            loop = list()
            
            dfs(i)
        
    print(n - len(ans))
