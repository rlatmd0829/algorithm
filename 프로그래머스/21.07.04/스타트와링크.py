n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]
curMin = 10000000
check = [False] * n


def recursive(index, count1, count2, sum1, sum2):
    global curMin
    if index == n:
        if count1 == count2:
            curMin = min(curMin, abs(sum1 - sum2))
        return
    # true : 1, 2
    # false : 0
    check[index] = True
    temp = 0
    for i in range(index):
        if check[i] == True:
            temp += graph[i][index] + graph[index][i]
    recursive(index+1, count1+1, count2, sum1+temp, sum2)

    check[index] = False
    temp = 0
    for i in range(index):
        if check[i] == False:
            temp += graph[i][index] + graph[index][i]
    recursive(index+1, count1, count2+1, sum1, sum2+temp)

recursive(0, 0, 0, 0, 0)
print(curMin)