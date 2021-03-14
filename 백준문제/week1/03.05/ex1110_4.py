N = input()

N = int(N)
cnt = 0
temp = N
while True:
    
    
    q1 =N % 10
    q2 = int(N/10)
    q3 = q1+ q2
    q3 = q3 % 10
    N = q1*10 + q3
   
    cnt = cnt +1
    if(N==temp):
        break
    

print(cnt)