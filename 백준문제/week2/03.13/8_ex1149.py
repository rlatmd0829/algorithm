# T = int(input())
# rgb = []

# for i in range(T):
#     rgb.append(list(map(int,(input().split()))))

# dp = [[0]*3 for i in range(T)]

# for i in range(T):
#     if i==0:
#         dp[i] = rgb[i]
#     else:
#         dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
#         dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
#         dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])


# print(min(min(dp[T-1][0], dp[T-1][1]), dp[T-1][2]))

# rgb (입력)
# 26 40 83
# 49 60 57
# 13 89 99

# rgb 
# 26 40 83
# 89 86 83
# 96 172 185

# 최적의해를 찾기 위해서 이전에 값에서 자신의 색깔을 제외한 두 색깔중 작은 값과 더해가면서 내려간다.
# 맨아래에서 가장 작은값이 최솟값이 된다.


T = int(input())
rgb = []

for i in range(T):
    rgb.append(list(map(int,(input().split()))))


for i in range(1,T):
    rgb[i][0] = rgb[i][0] + min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] = rgb[i][1] + min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] = rgb[i][2] + min(rgb[i-1][0], rgb[i-1][1])


print(min(rgb[T-1]))

    