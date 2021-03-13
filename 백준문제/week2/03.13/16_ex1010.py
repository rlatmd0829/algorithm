
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