

import sys
#sys.stdin = open("input.txt","rt")

N,K =  map(int,input().split())
List = list(map(int,input().split()))
res = set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(List[i]+List[j]+List[k])
res =  list(res)
res.sort(reverse=True)
print(res[K-1])