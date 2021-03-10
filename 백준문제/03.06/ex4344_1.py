c = int(input())


for i in range(c):
    sum = 0
    a = int(input())
    array = []
    for j in range(a):
        b = int(input())
        array.append(b)
        sum += b
    avg=int(sum / a)
    cnt = 0
    for k in array:
        if avg < k:
            cnt += 1
    result = cnt / a * 100
    print("%.3f%%"%result)
    
#############################################

c = int(input())

avg = []

for i in range(c):
    n = list(map(int, input().split()))
    sum=0
    for i in range(n[0]):
        sum += n[i+1]

    cnt=0
    for i in range(n[0]):
        if n[i+1] > (sum / n[0]):
            cnt +=1
    
    avg.append((cnt/n[0]) * 100) 

for i in range(c):
    print("%.3f" %avg[i] + "%")