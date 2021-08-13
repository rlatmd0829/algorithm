n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

count = []

for a in range(n-7):
    for b in range(m-7):
        w_count = 0 # W로 시작했을때 칠해야할 부분
        b_count = 0 # B로 시작했을때 칠해야할 부분
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 행과열에 합이 짝수, 홀수 일 경우가 같은 색상이다.
                    if graph[i][j] != 'W':
                        w_count += 1
                    if graph[i][j] != 'B':
                        b_count += 1
                else:
                    if graph[i][j] != 'B':
                        w_count += 1
                    if graph[i][j] != 'W':
                        b_count += 1
        print(w_count,b_count)
        count.append(min(w_count, b_count))
print(min(count))
