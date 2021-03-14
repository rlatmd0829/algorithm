# 유클리드 호제법 => 최대공약수 구하는 공식
# a,b의 최대공약수는 b와 a%b의 최대공약수와 같다
# 즉, GCD(a,b) = GCD(b,a%b)
# gcd(24,16) => gcd(16,8) => gcd(8,0)
# b가 0일때 gcd = a

# 최소공배수
# lcm = GCD * a/gcd * b/gcd

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

T = int(input())

for i in range(T):
    a,b = map(int,(input().split()))
    g = gcd(a,b)
    lcm = g * (a//g) * (b//g)
    print(lcm)


