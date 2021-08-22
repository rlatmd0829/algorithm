import collections
def solution(word, cards):
    n = len(cards)
    answer = -1
    word = list(word)
    graph =[]
    for card in cards:
        graph.append(list(card))
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    queue = collections.deque()
    
    def bfs(a,b):
        queue.append((a,b))
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny]
    return answer