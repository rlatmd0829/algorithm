
def solution(n, k):
    answer = 0
    graph = [0 for _ in range(n)]
    def dfs(x,cnt):
        nonlocal answer
        if cnt == k:
            answer += 1
        else:
            for i in range(n):
                if x == i:
                    continue
                else:
                    dfs(x,cnt+1)
    cnt = 0
    for i in range(2):
        cnt += 1
        for j in range(n):
            if cnt > 1:
                if j == 0:
                    continue
            dfs(j,0)
    answer = answer - (n-1)
    return answer % 10007