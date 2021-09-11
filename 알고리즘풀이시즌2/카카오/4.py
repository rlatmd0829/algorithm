def solution(n, info):
    answer = []
    score = [10,9,8,7,6,5,4,3,2,1,0]
    demo = {}
    info_total = 0
    for i in range(len(info)):
        temp = n
        result = [0] * len(info)
        total = 0
        
        for j in range(i, len(info)):
            if temp <= 0:
                break
            if temp > info[j]:
                result[j] = info[j]+1
                total += score[j]
                temp = temp - (info[j] + 1)
            else:
                info_total += score[j]
        if info_total < total:
            demo[total] = result
    ans = sorted(demo.items(), reverse = True)
    print(ans)
    if ans:
        answer = ans[0][1]
    else:
        return [-1]
    return answer