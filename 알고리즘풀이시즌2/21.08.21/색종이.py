n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
w_result = 0
b_result = 0
def recursive(x, y, n):
    global w_result, b_result
    w_cnt = 0
    b_cnt = 0

    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] == 0:
                w_cnt += 1
            if graph[i][j] == 1:
                b_cnt += 1 

    if w_cnt == (n * n):
        w_result += 1
    elif b_cnt == (n * n):
        b_result += 1

    else:
        recursive(x, y, n//2) # 1 사분면 0, 4, 0, 4
        recursive(x+n//2, y, n//2) # 2사분면 4, 8, 0, 4
        recursive(x, y+n//2, n//2) # 4사분면 0, 4, 4, 8
        recursive(x+n//2, y+n//2, n//2) # 3사분면 4, 8, 4, 8

    
recursive(0,0,n)
print(w_result)
print(b_result)


    
