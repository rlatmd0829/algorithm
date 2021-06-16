def binary(arr, target):
    min = 0
    max = len(arr) - 1
    
    
    while min <= max:
        mid = (min+max) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] >= target:
            max = mid - 1
        else:
            min = mid + 1
    return 0


n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for i in b:
    print(binary(b, i))

