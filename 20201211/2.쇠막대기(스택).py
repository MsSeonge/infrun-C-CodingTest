
import sys
sys.stdin = open("input.txt","rt")


string =  input()
stack = []
Sum =  0
for i in range(len(string)):
    if string[i]=='(':
        stack.append('(')
    elif string[i]==')':
        stack.pop()
        if string[i-1]=='(':
            Sum+=len(stack)
        else:
            Sum+=1
print(Sum)
