import sys
sys.stdin = open("input.txt","rt")
a = input()
stack = []
for x in a:
    if x.isdigit():
        stack.append(x)
    else: # 연산자일때
        a = int(stack.pop())
        b = int(stack.pop())
        if x =='+':
            stack.append(a+b)
        elif x =='-':
            stack.append(b-a)
        elif x =='/':
            stack.append(b/a)
        elif x =='*':
            stack.append(a*b)
print(stack.pop())




