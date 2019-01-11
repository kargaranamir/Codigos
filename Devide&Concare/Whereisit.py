from math import log10
def decrease(n):
    degree=0
    total=0
    for x in range(n-1):
        degree = degree +  int(log10(x+1)) + 1
        if (total + degree < n) :
            total += degree
        else:
            return n-total
def find(n):
    string=""
    i=0
    while(len(string) <n):
        i+=1
        string+=str(i)
    return string[n-1]
      #  Cstring=string
      #  string+=str(i+1)
      #  if(len(string)>n):
      #      return Cstring[n-1]

n = int(input())
print(find(decrease(n)))
