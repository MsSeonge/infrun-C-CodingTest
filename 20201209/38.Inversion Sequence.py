import sys
sys.stdin = open("input.txt","rt")

n  = int(input())
Map = list(map(int,input().split()))
Pre = [0] * n
print(Map)

for i in range(n,0,-1):
    cnt  = Map[i]
    val  = i
    if cnt ==0:
        Pre[i] = val
    else:
        for j in range(i,i+cnt,1):
            pass
