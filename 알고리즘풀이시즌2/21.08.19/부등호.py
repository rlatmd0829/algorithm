n = int(input())

bu = list(input().split())
check = [False] * 10
maxx = ""
minn = ""

def ch(i,j,k):
    if k == '>':
        return i > j
    if k == '<':
        return i < j

def recursive(index, sum):
    global maxx, minn
    if index == n+1:
        if len(minn) == 0:
            minn = sum
        else:
            maxx = sum
        return
    for i in range(10):
        if not check[i]:
            if index == 0 or ch(sum[-1], str(i), bu[index-1]):
                check[i] = True
                recursive(index+1, sum + str(i))
                check[i] = False

recursive(0,"")
print(maxx)
print(minn)
    
    
