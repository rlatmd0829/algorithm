
# math모듈 임포트하면 math.factorial() 사용가능

def fac(a):
    if a==0:
        return 1
    if a==1:
        return 1
    else:
        return a * fac(a-1)

# nCk = n! / ((n-k)! * k!)

T = int(input())
for i in range(T):
    n, m = map(int, input().split()) # m개중의 n개를 선택한다. mCn
    print(fac(m) // (fac(m-n) * fac(n))) 

# 다리가 겹쳐진다는 의미는 순서가 존재한다는 의미이기 때문에
# 조합에서는 순서가 없기 떄문에 애초에 포함이 안된다

# combinations 모듈을 사용하면 모든 조합의 수를 튜플로 담기 떄문에 느리다
# 이문제는 개수만 얻으면 되기 떄문에 사용안하는게 좋다.

# from itertools import combinations

# T = int(input())
# for i in range(T):
#     cnt = 0
#     n, m = map(int, input().split())

#     for j in combinations(range(1,m+1),n):
#         cnt += 1
#     print(cnt)
