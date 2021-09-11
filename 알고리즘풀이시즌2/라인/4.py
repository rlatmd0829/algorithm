import copy
def solution(n):
    answer = []
    arr = [[i for i in range(1,n+1)]]
    def prime_list(n):
        sieve = [True] * n
        m = int(n ** 0.5)
        for i in range(2, m+1):
            if sieve[i] == True:
                for j in range(i+i, n, i):
                    sieve[j] = False
        return [i for i in range(2, n) if sieve[i] == True]
    
    prime = prime_list(n)
    
    def exe(n, arr):
        p = 0
        for i in prime:
            if n % i == 0:
                p = i
                break
        demo = [[] for _ in range(p)]
        cnt = -1

        for i in range(len(arr)):
            cnt = (cnt + 1) % p
            demo[cnt].append(arr[i])
        
        return demo
    cnt = 0
    while True:
        result = []
        cnt += 1
        leng = len(arr[0])
        
        for i in range(len(arr)):
            demo = exe(leng, arr[i])
            result.extend(demo)
        
        arr = copy.deepcopy(result)
        result = []
        if len(arr[0]) == 1:
            break
        
    for i in arr:
        answer.append(i[0])
    return answer