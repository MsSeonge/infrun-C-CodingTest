import sys
sys.stdin = open("input.txt","rt")

n = int(input())
Map1 = list(map(int,input().split()))
m = int(input())
Map2 = list(map(int,input().split()))
ans = []

for x in Map1:
    if x in Map2:
        ans.append(x)
print(sorted(ans,reverse=False))
