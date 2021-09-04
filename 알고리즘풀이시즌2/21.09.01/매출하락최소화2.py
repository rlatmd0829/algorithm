# 트리 DP 문제같은데 DP 구현 못하겠다.

import collections
import sys
def solution(sales, links):
    INF = sys.maxsize
    answer = 0
    leng = len(sales)
    graph = [[] for _ in range(leng+1)]
    visited = [False for _ in range(leng+1)]
    distance = [0 for _ in range(leng+1)]
    dp = [[0, 0] for _ in range(leng+1)]
    # for i in range(leng):
    #     graph[i+1].append(sales[i])
    for a,b in links:
        graph[a].append(b)
    
    def dfs(cur):
        visited[cur] = True
        dp[cur][1] = sales[cur-1]
        dp[cur]
        result = []
        demo = 0
        for next in graph[cur]:
            if visited[next] == False:
                dfs(next)
                dp[cur][1] += min(dp[next][0], dp[next][1])
                if demo == 0:
                    demo = dp[next][1]
                elif demo > dp[next][1]:
                    demo = dp[next][1]
        dp[cur][0] += demo
            
    dfs(1)
    print(dp)
    print(min(dp[1][1], dp[1][0]))
                    
        
    return answer
sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))