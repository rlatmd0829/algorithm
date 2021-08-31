# answer 이랑 n이랑 같아지는 코드
# 2진수로 생각하니까 이해가 됐다.

n = int(input())

answer = 0
arr = 1
while n > 0:
    if n % 2 > 0: # 홀수인경우 이진수 자리값이 1인 경우에만 answer에 더해주면된다.
        answer += arr
        n -= 1 # 홀수인 경우 1을 빼줌 오른쪽 시프트 하면 없어지는값이라..?
    arr = arr * 2 # 2진수 자리값 증가
    n //= 2 # 2진수 오른쪽 시프트 같은 느낌

print(answer)