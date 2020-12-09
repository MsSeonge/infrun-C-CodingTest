
import sys
sys.stdin = open("input.txt","rt")


def binarySearch():
    start = Map[0]
    end =  sum(Map)
    ans = 2170000000
    while(start<=end):
        cnt = 1
        Sum = 0
        mid =  (start+end)//2
        for i in range(1,n+1):
            if Sum+i<=mid:
                Sum=Sum+i
            else:  # 크면
                Sum = i
                cnt+=1
        if cnt<=m:
            if mid<ans:
                ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans


n,m = map(int,input().split())
Map =  list(map(int,input().split()))
binarySearch()
print(binarySearch())
