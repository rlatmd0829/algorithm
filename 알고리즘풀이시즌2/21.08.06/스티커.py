t = int(input())

for i in range(t):
    n = int(input())
    st = [list(map(int,input().split())) for _ in range(2)]
    # 0 인덱스는 고유가지고 있는 값
    # 1 인덱스는 왼쪽 대각선의 합
    if n == 1:
        print(max(st[0][n-1], st[1][n-1]))
    else:
        st[0][1] += st[1][0]
        st[1][1] += st[0][0]
        for j in range(2, n):
            st[0][j] += max(st[1][j-1], st[1][j-2]) # 왼쪽 대각선을 선택하는 경우와 한칸더 왼쪽 대각선 선택하는 경우 
            st[1][j] += max(st[0][j-1], st[0][j-2])
        print(max(st[0][n-1], st[1][n-1]))
    

