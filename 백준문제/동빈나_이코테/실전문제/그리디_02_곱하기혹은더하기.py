array = input()

count = int(array[0])

for i in range(1, len(array)):
    num = int(array[i])
    if num <= 1 or count <= 1:
        count += num
    else:
        count = count * num

print(count)