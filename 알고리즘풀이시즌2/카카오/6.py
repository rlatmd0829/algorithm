from bisect import bisect_left, bisect_right
def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in skill:
        tp, r1, c1, r2, c2, degree = i
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if tp == 1:
                    board[x][y] -= degree
                else:
                    board[x][y] += degree
    
    for i in range(len(board)):
        board[i].sort()
        point = bisect_right(board[i], 0)
        # print(board[i])
        # print(len(board[i]))
        # print(point)
        answer += len(board[i]) - point
    return answer