import sys
MAX = 21 
# 어떤 값이 오든 20이 넘으면
# 결국 w(20, 20, 20) 을 호출하기
dp = [[[0] * MAX for _ in range(MAX)] for _ in range(MAX)]
# 재귀함수가 w(a, b, c 의 형태라면)
# 이것에 대한 값을 저장해야하는 것
def w(a, b, c):
    # 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 2
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 3
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    # 값을 찾으면 바로 반환한다.
    
    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    # while 끝내는 주문
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = ", w(a,b,c))