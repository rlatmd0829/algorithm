T = int(input())

def recursive(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    return recursive(num-1) + recursive(num-2) + recursive(num-3)

for i in range(T):
    print(recursive(int(input())))