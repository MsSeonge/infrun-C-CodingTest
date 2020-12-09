import sys
sys.stdin = open("input.txt","rt")


n = int(input())
Map1 = list(map(int,input().split()))
m = int(input())
Map2 = list(map(int,input().split()))
Map3 = [0]*(n+m)
pos1,pos2,pos3 = 0,0,0

while (pos1<n and pos2 <m):
    if Map1[pos1] < Map2[pos2]:
        Map3[pos3] = Map1[pos1]
        pos3+=1
        pos1+=1
    else:
        Map3[pos3] = Map2[pos2]
        pos3+=1
        pos2+=1
while(pos1<n):
    Map3[pos3] = Map1[pos1]
    pos3+=1
    pos1+=1
while(pos2<m):
    Map3[pos3] = Map2[pos2]
    pos3+=1
    pos2+=1
print(Map3)
