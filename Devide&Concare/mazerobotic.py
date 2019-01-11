n = int(input())
s=input()
x,y=input().split(' ')
m_x =int(x)
m_y=int(y)
x_n ,y_n = 0,0
for i in range(n):
    if(s[i]=='R'):
        x_n+=1
    elif(s[i]=='L'):
        x_n-=1
    elif(s[i]=='U'):
        y_n+=1
    elif(s[i]=='D'):
        y_n-=1
if (abs(m_x) + abs(m_y) > n or (n - abs(m_x) - abs(m_y)) % 2 == 1):
    print(str(-1))
elif (m_x-x_n == 0 and m_y-y_n==0):
    print(str(0))
else :
    print(str(3))
    
