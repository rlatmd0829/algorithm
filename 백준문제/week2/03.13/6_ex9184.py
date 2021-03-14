dp = [[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)] 
#dp = [[[0] * 21 for _ in range(21)] for _ in range(21)] #위와 똑같이 3중배열을 만든다.
print(dp)
def w(a,b,c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b >20 or c > 20:
        return w(20,20,20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = (w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c))
        return dp[a][b][c]
    else:
        dp[a][b][c] = (w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1))
        return dp[a][b][c]

while True:
    a,b,c = map(int,(input().split()))
    if a == -1 and b == -1 and c== -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

# 문제에 점화식이 쓰여져 있어서 그 점화식을 그대로 사용하면 된다.
# dp[] 3중 리스트를 만들어서 값을 저장할 수 있게 해준다. 범위는 20이 넘어가게 되면 다 20으로 만들고 음수가 되면 바로 1을 리턴해주기 때문에
# 인덱스 0~20 까지 쓸수 있도록 21로 잡는다.

# dp[a][b][c] 가 처음 들어온 값인지 기존에 저장이 되어있는 값인지 확인해준다.
# 이 확인문이 위에 20보다 클경우 전부 20으로 바꿔주는 확인문 아래에 있어야 리스트 범위 초과 에러가 안난다.
