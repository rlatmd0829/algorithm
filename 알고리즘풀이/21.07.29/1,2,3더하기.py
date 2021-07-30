# T = int(input())
# testList = []

# for _ in range(T):
#     testList.append(int(input()))

# maxNum = max(testList)

# dp=[1,2,4]

# for i in range(3,maxNum+1):
#     dp.append(dp[i-3] + dp[i-2] + dp[i-1])

# for num in testList:
#     print(dp[num-1])


####

t = int(input())
result = [int(input()) for _ in range(t)]

dp = [0 for _ in range(max(result)+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max(result)+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in result:
    print(dp[i])