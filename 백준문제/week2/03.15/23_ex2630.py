def quad_tree(x, y, n):
    global blue, white
    color = matrix[y][x] # 리스트에서 [][] 앞에 값이 이중리스트 안에 어떤 리스트인지를 결정하기때문에 좌표개념에 y랑 같은뜻이다.
    double_break = False
    
    for i in range(x, x+n):
        if double_break:
            break
                # [ [],[],[] ] list[0][1]
        for j in range(y, y+n):
            if matrix[j][i] != color: # 하나라도 틀릴시에 재귀문 생성
                quad_tree(x, y, n//2) # 2사분면
                quad_tree(x + n//2, y, n//2) # 1사분면
                quad_tree(x, y + n//2, n//2) # 3사분면
                quad_tree(x + n//2, y + n//2, n//2) # 4사분면
                double_break = True # 탈출
                break
        
    if not double_break: # double_break가 false일 경우
        if matrix[y][x] == 1: # 파란색이라면 ,,,, 이해가 잘안감
            blue += 1
        else:
            white += 1 # 흰색이라면

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]


blue = 0
white = 0

quad_tree(0,0,N)
print(white)
print(blue)

# 분할정복과 동적계획법은 비슷하지만 다른 개념이다.
# 일단 둘 다 반복과 재귀를 이용하며 Top-down 이나 Bottom-up방식을 통해서 문제를 해결한다.
# 동적 계획법은 작게 나눈 부분들을 해결해가면서 결과를 더 큰 부분을 푸는데 이용한다.
# 이때 분할되는 과정에서 작은 부분들이 중복되어서 여러 번 반복되어 나올 수 있기 때문에 memoization도 같이 사용한다.
# 분할 정복도 문제를 풀 수 있는 가장 작은 단위의 문제로 만든 다음에 해결하고 병합하는 과정들을 한다.
# 차이점은 동적 계획법과 달리 sub problems의 중복이 없다.