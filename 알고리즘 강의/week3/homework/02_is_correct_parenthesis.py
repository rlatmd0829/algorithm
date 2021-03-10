s = "(((("


def is_correct_parenthesis(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!