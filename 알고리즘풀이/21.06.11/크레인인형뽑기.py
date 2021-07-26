def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
        for j in range(len(result)-1):
            if result[j] == result[j+1]:
                result.pop()
                result.pop()
                answer += 2
                break
    return answer