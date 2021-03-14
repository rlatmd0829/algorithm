n = int(input())
my = list(map(int,input().split()))

m = int(input())
ch = list(map(int,input().split()))

my.sort()


result=[]

def ee(target, array):
    left = 0
    right = len(array)-1
    mid = (left +right) //2

    while left <= right:
        if target < array[mid]:
            right = mid-1
        elif target == array[mid]:
            return 1
        else:
            left = mid+1
        mid = (left + right) //2
    return 0

for i in ch:
    result.append(ee(i,my))
    

for i in result:
    print(i, end=' ')


