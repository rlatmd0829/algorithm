n = int(input())

array = list(map(int,input().split()))
print(array)

array.sort()
count = 0
result = 0
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)