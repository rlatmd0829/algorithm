def solution(s):
    answer = 99999999
    for i in range(1, len(s)//2 + 1):
        ret = ""
        count = 1
        prev = s[:i]
        for j in range(i, len(s)+i, i):
            if prev == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    ret = ret + str(count) + prev
                else:
                    ret = ret + prev
                prev = s[j:j+i]
                count = 1
        answer = min(answer, len(ret))
    return min(answer, len(s))