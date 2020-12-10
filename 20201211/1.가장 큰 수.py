import sys
sys.stdin  =open("input.txt","rt")

#파이썬은 스택이 따로 필요없다 리스트 자체가 스택역할  
for i in range(2):
    num, m = map(int, input().split())
    num = list(map(int, str(num)))
    stack = []
    for x in num:
        while stack and m>0 and stack[-1]<x: #스택이 존재하고 3회보다적고 스택의 마지막 인덱스가 x보다 작을때
            stack.pop()
            m-=1
        stack.append(x)
    if m!=0:
        stack  = stack[:-m]
    res =''.join(map(str,stack))
    print(res)
