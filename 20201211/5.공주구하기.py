from collections import deque
import sys
sys.stdin = open("input.txt","rt")


n,m = map(int,input().split())
Map = list(range(1,n+1))
Q =  deque(Map)

while Q:
    temp = m
    for i in range(m-1):
        x = Q.popleft()
        Q.append(x)
    Q.popleft()
    if len(Q)==1:
        break
print(Q.pop())
