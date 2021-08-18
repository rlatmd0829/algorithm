def square(x,y):  # 작은 사각형 나누기
    return (x//3)*3 + (y//3)

def recursive(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str,row)))
        return True
    x = z//n # 행
    y = z%n # 열
    if a[x][y] != 0:
        return recursive(z+1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[square(x,y)][i] == False:
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                a[x][y] = i
                if recursive(z+1):
                    return True
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = False
    return False


n = 9
a = [list(map(int,input().split())) for _ in range(n)]
c = [[False]*10 for _ in range(n)]
c2 = [[False]*10 for _ in range(n)]
c3 = [[False]*10 for _ in range(n)] # 스도쿠는 행, 열, 사각형이 모두 1~9로 채워져있어야한다.

for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True # 행에 1~9 나온값은 True로 체크
            c2[j][a[i][j]] = True # 열에 1~9 나온값은 True로 체크
            c3[square(i,j)][a[i][j]] = True
recursive(0)