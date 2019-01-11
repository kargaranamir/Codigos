[a,b]= [int(x) for x in input().split()]
heap_wintree=[]
lst2=[]
count=0
j=0
for i in range (1,a+1): 
    heap_wintree.append([int(x) for x in input().split()])

while(1):
    if count==b:
        print(save)
        break
    else :
        firstelements=[item[0] for item in heap_wintree ]
        j=firstelements.index(min(firstelements))
        save=heap_wintree[j][0]
        del heap_wintree[j][0]
        if (save):
            count+=1
        else :
            heap_wintree = [x for x in heap_wintree if x != []]
