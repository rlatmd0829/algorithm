def solution(gems):
    answer = []
    set_gems = set(gems)
    leng = len(set_gems)
    l, r = 0,0
    dict_gems = {}
    minn = len(gems) + 1
    
    while True:
        if r == len(gems):
            break
        
        if gems[r] not in dict_gems:
            dict_gems[gems[r]] = 1
        else:
            dict_gems[gems[r]] += 1
        r += 1
        
        if len(dict_gems) == leng:
            while True:
                if dict_gems[gems[l]] > 1:
                    dict_gems[gems[l]] -= 1
                    l += 1
                elif r - l < minn:
                    minn = r - l
                    answer = [l + 1, r]
                    break
                else:
                    break
        
    return answer