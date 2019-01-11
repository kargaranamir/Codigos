(n,k)= (int(x) for x in input().split())
if (n >500 or k >500):
    exit(0)
C=[int(x) for x in input().split()]
subset = [[0 for x in range(k+1)] for y in range(k+1)] 
subset[0][0] = 1
for c in C:
    for i in range(k,-1,-1):
        if(i-c<0):
            break
        for x in range (k+1):
            if (subset[i-c][x]):
                subset[i][x],subset[i][x+c]=1,1
print(sum(subset[k]))
print(*[i for i, e in enumerate(subset[k]) if e == 1])
