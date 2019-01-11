(m,s)= (int(x) for x in input().split())
s_copy=s

def find(m,s,s_copy):
    str1=""
    while(len(str1)<m):
        if (s_copy>9):
            str1+="9"
            s_copy-=9
        else:
            str1+='{}'.format(s_copy)
            s_copy=0        
    str2=""
    s_copy=s
    while(len(str2)<m):
        if (s_copy>9):
            str2+="9"
            s_copy-=9
        else:
            if(len(str2)<m-1): #false result for m
                str2+='{}'.format(s_copy-1)
                s_copy=1
                while(len(str2)<m-1): #false result for m
                    str2+='{}'.format(~s_copy+1+1)
                str2+='{}'.format(s_copy)              
            else:
                str2+='{}'.format(s_copy)
        str2=str2[::-1]
    print(str(str2)+' '+str(str1))


if(m == 1 and s == 0):
    print("0 0")
elif (s == 0 or s > 9*m ):
    print("-1 -1")
else :  
    find(m,s,s_copy)

