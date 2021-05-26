n, m = map(int,input().split())

array = list(map(int, input().split()))

count = 0
for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            continue
        else:
            count+=1
print(count)