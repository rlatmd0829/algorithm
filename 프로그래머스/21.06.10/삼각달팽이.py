def solution(n):
    answer = [[0 for j in range(i+1)] for i in range(n)]
    result = []
    x,y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            #down
            if i % 3 == 0:
                x += 1
            #right
            elif i % 3 == 1:
                y += 1
            #up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    for i in range(n):
        for j in range(i+1):
            result.append(answer[i][j])
    return result