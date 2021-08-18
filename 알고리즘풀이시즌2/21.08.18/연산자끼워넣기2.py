import sys
n = int(input())

value = list(map(int, input().split()))
calc = list(map(int, input().split())) # +,-,*,//
maxx = -(sys.maxsize)
minn = sys.maxsize
sum = value[0]
def recursive(index, sum, plus,minus,mul,div):
    global maxx, minn

    # 정답을 찾은 경우
    if index == n:
        maxx = max(maxx, sum)
        minn = min(minn, sum)
        return

    #if plus + minus + mul + div 


    # 불가능한 경우
    # 이 문제는 불가능한 경우가 없다.
    # 연산자가 n-1개 주어지고 연산자 넣는곳도 n-1개가 있기때문

    if plus > 0:
        recursive(index+1, sum+value[index],plus-1,minus,mul,div)
    if minus > 0:
        
        recursive(index+1, sum-value[index],plus,minus-1,mul,div)
    if mul > 0:
        
        recursive(index+1, sum*value[index],plus,minus,mul-1,div)
    if div > 0:
        if sum >= 0:
            recursive(index+1, sum//value[index],plus,minus,mul,div-1)
        else:
            recursive(index+1, -(-sum//value[index]),plus,minus,mul,div-1)
recursive(1,sum,calc[0],calc[1],calc[2],calc[3])
print(maxx)
print(minn)