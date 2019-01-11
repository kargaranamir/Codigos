def merge_lists(l):
        s=list(map(set, l))
        i, n=0, len(s)
        while i < n-1:
                for j in range(i+1, n):
                        if s[i].intersection(s[j]):
                                s[i].update(s[j])
                                del s[j]
                                n-=1
                                break
                else:
                        i+=1
        return len(s)
l=[]
n=int(input())
for x in range (1,n+1) :
    l.append([x])
while (1):
    [a,b]= [int(x) for x in input().split()]
    if a==0 and b==0:
            break
    else :
        l.append([a,b])
print(merge_lists(l))
