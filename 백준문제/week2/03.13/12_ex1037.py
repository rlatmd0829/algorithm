N = int(input())

q = list(map(int, input().split()))
q.sort()
result = q[0] * q[-1]
print(result)

# 어떤 수 N의 진짜 약수가 모두 주어질때 N을 구하라
# 약수에 제일 작은 값과 제일 큰값을 곱하면 N을 구할 수 있다
# 정렬 해준뒤 [0] 값과 [-1]값을 곱해준다.
