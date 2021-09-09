import sys
sys.setrecursionlimit(10**7)
answer = 0
def solution(n, k):
    
    graph = [[0 for _ in range(n)] for _ in range(n)]
    def dfs(x,y,cnt):
        global answer
        if cnt == k:
            answer += 1
        else:
            for i in range(n):
                for j in range(n):
                    if x == i or y == j:
                        continue
                    else:
                        dfs(x,y,cnt+1)
    for i in range(n):
        for j in range(n):
            dfs(i,j,1)
    print(answer//2)
    
    return (answer//2) % 10007