answer = 0
def solution(word, cards):
    n = len(cards)
    
    word = list(word)
    graph =[]
    check = [[0]*n for _ in range(n)]
    for card in cards:
        graph.append(list(card))
        
    def chk(i,j):
        for a in range(n):
            for b in range(n):
                if i == a or j == b:
                    if check[a][b] == 1:
                        return False
        return True
        
    def dfs(x):
        global answer
        if x == n:
            answer += 1
        else:
            for i in range(n):
                for j in range(n):
                    if graph[i][j] in word:
                        if chk(i,j):
                            check[i][j] = 1
                            word.remove(graph[i][j])
                            dfs(x+1)
                            check[i][j] = 0
                            word.append(graph[i][j])
                            print(word)
                        
    dfs(0)
    return answer

word = "APPLE"
cards = ["LLZKE", "LCXEA","CVPPS","EAVSR","FXPFP"]
print(solution(word, cards))
