from collections import deque
import sys
sys.stdin  = open("input.txt","rt")



need = input()
n = int(input())
for  i in range(n):
    plan  = input()
    Q =  deque(need)
    for x in plan:
        if x in Q:
            if x!=Q.popleft():
                print("#%d NO" %(i+1))
                break
    else: #이런식으로  else 구현 가능  
        if len(Q)==0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))