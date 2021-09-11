import collections
def solution(board, aloc, bloc):
    answer = -1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    row = len(board)
    col = len(board[0])
    queue = collections.queue()
    queue.append(aloc)
    queue.append(bloc)
    def bfs():
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < row and 0 <= ny < col:
                    if board[nx][ny] == 0:
                        board[x][y] = 0
                        queue.append([nx,ny])
    return answer