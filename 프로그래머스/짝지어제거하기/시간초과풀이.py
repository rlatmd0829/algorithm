def solution(s):
    answer = -1
    s = list(s)
    i = -1
    
    while s:
        
        i += 1
        if i == len(s)-1:
            break
            
        if s[i] == s[i+1]:
            #s = s[:i] + s[i+2:]
            s.pop(i)
            s.pop(i)
            i = -1
    
    if s:
        return 0
    else:
        return 1