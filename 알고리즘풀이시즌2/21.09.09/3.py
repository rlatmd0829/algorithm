answer = 0
def solution(n, k):
    
    row = [0] * n
    #graph = [[0 for _ in range(n)] for _ in range(n)]
    def dfs(x):
        global answer
        if x == n:
            answer += 1
        else:
            for i in range(n):
                row[x] = i
                print(row)
                for j in range(x):
                    if row[j] == row[x]:
                        break
                    else:
                        dfs(x+1)
    dfs(0)
    
    return answer