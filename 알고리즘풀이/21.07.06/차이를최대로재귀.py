n = int(input())

nums = list(map(int, input().split()))
check = [False] * n
order = [0] * n
curMax = 0
def recursive(index):
    global curMax
    if index == n:
        sum = 0
        for i in range(1, n):
            sum += abs(nums[order[i]] - nums[order[i-1]])
        curMax = max(sum, curMax)
        return

    for i in range(n):
        if check[i] == False:
            order[index] = i
            check[i] = True
            recursive(index+1)
            check[i] = False

recursive(0)
print(curMax)
    
    
