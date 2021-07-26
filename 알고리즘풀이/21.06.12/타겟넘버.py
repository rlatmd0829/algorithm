def solution(numbers, target):
    answer = 0
    a=[0]
    for i in numbers:
        b=[]
        for j in a:
            b.append(j+i)
            b.append(j-i)
        a=b
    return a.count(target)