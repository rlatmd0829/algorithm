n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
w_result = 0
b_result = 0
def recursive(r, n_r, c, n_c, n):
    global w_result, b_result
    w_cnt = 0
    b_cnt = 0

    for i in range(r,n_r):
        for j in range(c,n_c):
            if graph[i][j] == 0:
                w_cnt += 1
            if graph[i][j] == 1:
                b_cnt += 1 

    if w_cnt == (n * n):
        w_result += 1
        
    elif b_cnt == (n * n):
        b_result += 1
    elif n == 1:
        return
    else:
        recursive(r, r+n//2, c, c+n//2, n//2) # 1 사분면 0, 4, 0, 4
        recursive(r, r+n//2 , c+n //2 , c+n, n//2) # 2사분면 4, 8, 0, 4
        # (0,4,0,4)
        # (0,2,2,4)
        # (0,1,2,4)
        #recursive(0,8,0,8)
        #recursive(4, 8, 0, 4) n =4 
        #recursive(2, 4, 0, 2) n = 2


        recursive(r+n//2, r+n, c, c+n//2, n//2) # 4사분면 0, 4, 4, 8


        #recursive(0,8,0,8)
        #recursive(0, 4, 4, 8) n =4
        #recursive(0, 2, 2, 4) 


        recursive(r+n//2, r+n, c+n//2, c+n, n//2) # 3사분면 4, 8, 4, 8

    
recursive(0,n,0,n,n)
print(w_result)
print(b_result)


    
