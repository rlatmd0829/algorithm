import sys
input = sys.stdin.readline
arr = []
dp = []

N = int(input())
for _ in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0]+arr[1])
else:
    dp.append(arr[0])
    dp.append(max(arr[0]+arr[1], arr[1]))
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

    for i in range(3, N):
        dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1]))

    print(dp.pop())

# 도착점은 무조건 밟아야 하기때문에 2가지 경우가 올 수 있다.
# 첫째, 도착점에서 한칸전(n-1) 계단을 밟고 올라온 경우이며 이럴 땐 세번 연속 계단을 오를 순 없으므로
# 그 이전 계단은 그 전전인 (n-3)번째 계단이 된다.

# 둘째, 두칸 전(n-2) 계단을 밟고 올라온 경우이다.

# dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])) 두값중 큰값을 dp에 저장해주면 된다.
# 인덱스가 i-3이 있기 떄문에 에러가 나지 않도록 3까지는 dp에 미리 넣어준다.