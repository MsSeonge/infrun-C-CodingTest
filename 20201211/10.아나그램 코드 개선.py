import sys
sys.stdin  = open("input.txt","rt")

a=input()
b=input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x,0)+1
for x in b:
    str1[x] =str1.get(x,0)-1

for x in a:
    if str1.get(x)>0:
        print("NO")
        break
else:
    print("YES")