array = input()

left = 0
right = 0
count=len(array)//2
for i in array:
    
    if count != 0:
        left += int(i)
        count -= 1
    else:
        right += int(i)
print(left)
print(right)
if left == right:
    print("LUCKY")
else:
    print("READY")
    

# left_count = 0
# right_count = 0
# for i in range(0, len(array)//2):
#     left_count += array[i]

# for i in range(len(array)//2, len(array)):
#     right_count += array[i]

# print("left",left_count)
# print("right",right_count)
# if left_count == right_count:
#     print("LUCKY")
# else:
#     print("READY")