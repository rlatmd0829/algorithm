a ,b = map(int, input().split())

m=max(a,b) # 두 수 중에 큰 값을 골라 범위로 지정
k = 2 # 1로 나눠지는 것을 피하기 위해 2부터 시작
gcd = 1
while k<=m:
    if a%k==0 and b%k==0: 
        if gcd < k: # 두 수 모두 나눠지는 수 중에 가장 큰값을 찾는다
            gcd = k # gcd = 최대공약수 = 두수 모두 나눠지는 수 중 가장 큰값
    k +=1 

lcm = gcd * (a // gcd) * (b // gcd) # lcm = 최소공배수
# 최소공배수 = 6 | 24 18
#               ㅡㅡㅡㅡ
#                  4  3    => 6 * 4 * 3

print(gcd)
print(lcm)


###################################################

