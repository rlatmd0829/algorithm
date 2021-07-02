
height = [int(input()) for _ in range(9)]
total = sum(height)
for i in range(9):
    for j in range(i+1, 9):
        if total - (height[i] + height[j]) == 100:
            print('--------------')
            print(i)
            print(j)
            print(height[i])
            print(height[j])
            print(height)
            height.remove(height[i])
            print(height)
            height.remove(height[j])
            print(height)
            print('--------------')
            break
    if len(height) < 9:
        break
height.sort()
for i in height:
    print(i)

