def solution(s):
    answer = ''
    list_s = list(map(int,s.split(" ")))
    answer = str(min(list_s)) + " " + str(max(list_s))
    return answer

# 알고리즘