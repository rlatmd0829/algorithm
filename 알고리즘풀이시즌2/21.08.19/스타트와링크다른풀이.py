N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [False]*N
curMin = 1000000
def recursive(index, howMany, curSum):
    global curMin
    if index == N:
        if howMany != N/2:
            return
        else:
            sum = 0
            for x in range(N):
                if check[x] == False:
                    for xx in range(x):
                        if check[xx] == False:
                            sum += graph[x][xx] + graph[xx][x]
            curMin = min(curMin, abs(sum-curSum))
            return
    check[index] = True
    addSum = 0
    for i in range(index):
        if check[i] == True:
            addSum += graph[index][i]
            addSum += graph[i][index]
    recursive(index+1, howMany+1, curSum + addSum)
    check[index] = False
    recursive(index+1, howMany, curSum)
recursive(0, 0, 0)
print(curMin)