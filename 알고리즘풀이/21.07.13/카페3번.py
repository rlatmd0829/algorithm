line1 = "abbbcbbb"
line2 = "bbb"

tx1 = []
tx2 = []

for i in range(0, 101):
    if len(('_'*i).join(line2)) >= len(line1):
        break
    str = ('_'*i).join(line2)
    for i in range(len(line1)):
        if str[i] == '_':
            continue
        else:
            tx1.append(str[i])
            tx2.append(line2[i])
    print(tx1,tx2)

if tx1 == tx2:
    print(True)
else:
    print(False)
    
