a = 1
def test():
    global a
    a= 3
    b=2

    return a+b
# sum = 0
# for i in range(5):
#     sum += i

print(test())
print(a)