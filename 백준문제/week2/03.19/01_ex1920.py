
def two(arr, target):
    Min = 0
    Max = len(arr)-1
    
    while Min <= Max:
        Mid = (Max+Min) // 2
        if arr[Mid] == target:
            return 1
        elif arr[Mid] >= target:
            Max = Mid - 1
        else:
            Min = Mid + 1
    return 0


N = int(input())
node = list(map(int, input().split())) # N = 5 , node = [1,2,3,4,5]
M = int(input())
check = list(map(int, input().split()))
node.sort()

for i in check:
    print(two(node, i))