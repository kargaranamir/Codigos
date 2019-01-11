def maxCoins(coins,f):
    result=0
    selected_coin=0
    #selected_coin =1  Test caseetoon kharabe !!!! va ba 1 shoroo nemishe!!!
    for c in range(0,f-1):
        #if sum(coins[0:c])<coins[c+1]:
        if selected_coin + coins[c]<coins[c+1]:
            selected_coin = selected_coin + coins[c]
        
            result = result +1
    return(result+1)

    
def main(): 
    T =int (input())
    for x in range(T):
        f=input()
        c=input()
        coins=list(map(int, c.split()))
        #print(coins)
        ans=maxCoins(coins,int(f))
        print(ans)
if __name__ == '__main__': 
    main() 
