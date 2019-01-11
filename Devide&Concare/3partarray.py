n = int(input())
arr= [int(x) for x in input().split()]
x,ans,sum1,sum3 = 0,0,0,0
while (x < n+1):
    if (sum1 < sum3):
        sum1 += arr[x]
        x+=1
    else:
        n-=1
        sum3 += arr[n];	
    if (x < n+1 and sum1 == sum3):
        ans = max(ans, sum1)
print(ans)
