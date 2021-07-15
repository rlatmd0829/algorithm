a = [1,2,3,4]

def plus_one(x):
    return x+1

print(list(map(plus_one, a)))
print(list(map(lambda x : x+1, a)))