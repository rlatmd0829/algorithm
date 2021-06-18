def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    count_0 = 0
    for i in lottos:
        if i == 0:
            count_0 += 1
        elif i in win_nums:
            count += 1
    total = count + count_0
    return answer[total],answer[count]