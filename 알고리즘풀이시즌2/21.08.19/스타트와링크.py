import sys
input = sys.stdin.readline
n = int(input())
check = [False] * n
team = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
def recursive(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0,0
        for i in range(n):
            for j in range(i):
                if check[i] and check[j]:
                    start += team[i][j] + team[j][i]
                elif not check[i] and not check[j]:
                    link += team[i][j] + team[j][i]
        ans = min(ans, abs(start - link))
    
    for i in range(idx, n):
        if check[i]:
            continue
        check[i] = True
        recursive(i+1, cnt+1)
        check[i] = False

recursive(0,0)
print(ans)

