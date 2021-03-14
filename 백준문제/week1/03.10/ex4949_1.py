

while True:
    s = input()
    
    if s == '.':
        break
    stack = []
    answer = True

    for i in s:
        
        if i =='(' or i == '[':
            stack.append(i)
            
        elif i == ')':
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == '(':       
                stack.pop()
            else:
                answer=False
                break
        elif i ==']':
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                answer = False
                break
    
    
    if answer and not stack:
        print("yes")
    else:
        print("no")

