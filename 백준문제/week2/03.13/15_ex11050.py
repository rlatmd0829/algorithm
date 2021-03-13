# (n)  ==> nCk = n! / ((n-k)! * k!) 이항계수와 조합이 같은개념 같다
# (k)  ==>      

# nCr n개의 원소 중 r개의 원소를 뽑아내는 경우의 수를 말한다
# nCr = n-1Cr-1 + n-1Cr
# 즉 이미 n번째 원소를 선택했다고 가정하고 나머지 원소 중에서 r-1을 뽑는 것과
# n번째 원소를 제외한 나머지 중에서 r개의 원소를 뽑는 경우의 합이다 (무슨말인지 이해가 잘안감)

n , k = map(int,input().split())

def fac(a): # k가 입력값으로 0이 들어올 수 있으므로 0에대한 처리도 해줘야한다.
    if a== 0 :
        return 1
    if a == 1:
        return 1
    else:
        return a * fac(a-1)

print(fac(n) // (fac(n-k) * fac(k)))

