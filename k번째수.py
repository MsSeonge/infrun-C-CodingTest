
import sys
sys.stdin = open("input.txt", "rt")
TestCase  = int(input())
for  i in range(1,TestCase+1):
    N, s, e, k = map(int, input().split())
    List = list(map(int,input().split()))
    sortedList = List[s-1:e]
    sortedList.sort()
    #print("#"+str(i)+" "+str(sortedList[k-1]))
    #
    #내가해야하는 출력방식
    print("#%d %d" %(i, sortedList[k-1]))
