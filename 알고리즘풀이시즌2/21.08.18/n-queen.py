def check(row, col): # 행에는 무조건 한개만 놓기때문에 check할 필요없다.
    if check_col[col]: # 같은 열에 True가 있다면 놓을수 없다
        return False
    if check_dig[row+col]: # 같은 대각선에 True가 있다면 놓을수 없다.
        return False
    if check_dig2[row-col+n-1]: # 같은 대각선에 True가 있다면 놓을수 없다.
        return False
    return True

def calc(row): 
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            graph[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            graph[row][col] = False
    return ans

n = int(input())
graph = [[False]*n for _ in range(n)]
check_col = [False]*n # 열
check_dig = [False]*(2*n-1) # \ 대각선
check_dig2 = [False]*(2*n-1) # / 대각선
print(calc(0))