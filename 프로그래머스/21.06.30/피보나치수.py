
cache = {}
def fibo(num):
    if(num == 1):
        return 1
    elif(num == 2):
        return 1

    # 캐시에 값이 있다면 바로반환
    if(num in cache):
        return cache[num]
    # 답을 구했다면, cache에 저장
    cache[num] = fibo(num-1) + fibo(num-2)
    
    return cache[num]

print(fibo(int(input())))