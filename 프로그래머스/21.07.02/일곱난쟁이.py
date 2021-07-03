
height = [int(input()) for _ in range(9)]
total = sum(height)
for i in range(9):
    for j in range(i+1, 9):
        if total - (height[i] + height[j]) == 100:
            num1, num2 = height[i], height[j] # 값을 저장해두는 이유는 한개를 제거하게 되면 인덱스가 바뀌므로 값이 달라지기 때문에 삭제하기 전에 미리 저장을 해둔다.

            height.remove(num1) # pop()으로 삭제하면 인덱스가 달라지게 되면 값이 달라지므로 remove로 값으로 삭제를 하고 값은 삭제하기 전에 미리 다른 곳에 넣어둬서 한개를 삭제했을때 값이 달라져도 remove로 삭제할 수 있게 해준다.
            height.remove(num2)
            break
    if len(height) < 9:
        break
height.sort()
for i in height:
    print(i)

