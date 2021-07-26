def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        i = format(i, 'b').zfill(n)
        j = format(j, 'b').zfill(n)
        result = ''
        for a,b in zip(i,j):
            if int(a) + int(b) >= 1:
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer