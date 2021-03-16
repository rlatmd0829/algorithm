# N = int(input())
# arr = list(map(int, input().split()))
# result = [1] * N
# for i in range(1,N):
#     for j in range(i):
#         if arr[j] < arr[i]:
#             result[i] = max(result[i], result[j]+1)

# print(max(result))


###########################

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]: # 증가하는 부분수열을 이어줄려면 a[i]보다 작은 값중에 가장 긴 증가하는 수열에 값을 dp[i]에 저장한다. 
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))