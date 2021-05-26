array = input()
result = 0
newArray = []
for i in array:
    data = ord(i)
    if data >= 48 and data <= 57:
        result += int(i)
    else:
        newArray.append(i)
newArray.sort()
newArray.append(str(result))
print(''.join(newArray))