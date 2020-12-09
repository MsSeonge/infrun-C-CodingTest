import sys
sys.stdin = open("input.txt","rt")
a = int(input())
tmp = a
a = a-1
b=1
cnt =0
while(a>0):
    b+=1
    a=a-b  # 12
    if a % b == 0:   #  12  % 2 = =0
        for i in range(1,b):  #
            print(i+(a//b)," + ",end='')
        print(b+(a//b)," = ",tmp)
