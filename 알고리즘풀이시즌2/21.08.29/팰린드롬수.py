while True:
    value = input()
    if value == '0':
        break
    result1 = []
    result2 = []
    for i in range(len(value)):
        result1.append(value[i])

    for i in range(len(value)-1, -1, -1):
        result2.append(value[i])
    
    
    if ''.join(result1) == ''.join(result2):
        print("yes")
    else:
        print("no")