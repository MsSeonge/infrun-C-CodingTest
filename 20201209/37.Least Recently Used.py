

n,m  = map(int,input().split())
Map = list(map(int,input().split()))
cashe = [0] * (n);

for i in range(m): # 0~ 8번까지
    pos = -1
    a = Map[i]
    if a in cashe:  # Hit
        pos = cashe.index(a)
        for j in range(pos,0,-1):
            cashe[j] = cashe[j-1]
        cashe[0] = a
    else:  # Miss
        cashe.insert(0,a)
        cashe.pop()
print(cashe)



