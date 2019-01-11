class Stack:
    def __init__(self):
        self.stack = list()
        self.maxSize = 40
        self.top = 0

    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
        
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
        
    def size(self):
        return self.top

def findCelebrity(matrix,n):
    s= Stack()
    C=0
    A=0
    B=0
    for i in range(n-1):
        s.push(i)   
    A=s.top
    s.pop()
    B=s.top
    s.pop()
    while(s.size() >1):
        try :
            if (matrix[A][B]):
                A=s.top
                s.pop()
            else :
                B=s.top
                s.pop()
        except IndexError:
            B=s.top
            s.pop()
                   
    C=s.top
    s.pop()
    try : 
        if (matrix[C][B]):
            C=B
    except IndexError:
        pass
    try :
        if (matrix[C][A]):
            C=A
    except IndexError:
        pass
    
    for i in range (n):
        if ((i != C) and (matrix[C][i]==1 or matrix[i][C]==0)):
            return -1
    return C

    


def main():
    n= int(input()) 
    matrix = []
    for i in range(n):
        matrix.append([int(j) for j in input().split()])
    count=findCelebrity(matrix,n)
    if count==-1:
        print("There's no celebrity in this party!")
    else :
        print("Person "+str(count)+" is a celebrity!")


if __name__ == '__main__': 
    main()
