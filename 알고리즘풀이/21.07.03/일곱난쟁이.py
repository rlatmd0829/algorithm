height = [int(input()) for _ in range(9)]
check = [False] * 9
result = []
def recursive(index):
    global result
    if index == 9:
        answer = 0
        count = 0
        demo = []
        for i in range(9):
            if check[i]:
                answer += height[i]
                count += 1
                demo.append(height[i])
        if answer == 100 and count == 7:
            demo.sort()
            result = demo
        return
    
    check[index] = True
    recursive(index + 1)

    check[index] = False
    recursive(index + 1)

recursive(0)
for i in result:
    print(i)
