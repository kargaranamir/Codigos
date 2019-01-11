class CircularQueue:

    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 8

    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True


    def dequeue(self):
        if self.size()==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data


    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))
    def printQueue(self):
        return self.queue
  
def find(a,n):
    remaining_petroleum=0
    flag=0
    for i in range(n-1):
        if (a.size()!=0):
            falg=1
            ab=a.dequeue()
        #    print(a.printQueue())
            remaining_petroleum += int(ab[0])
            remaining_petroleum -= int(ab[1])
        #    print(remaining_petroleum)
            if (remaining_petroleum <0):
           #     print("amir")
           #     print(a.head)

                return 0
        else :
            if(remaining_petroleum <0):
           #     print("amir2")
                return 0
            elif (flag) :
            #    print("amir3")
                return 1
    return 1
        
        
def main():
    a=CircularQueue()
    n = int(input())
    for i in range(n):
        a.enqueue(list(map(int,input().strip().split())))
    x=0
    for i in range(n-1):
        if (x!=n):
            if (find(a,n)==1):
                print("You should start at "+str(x)+"!")
                return 0
            else :
                x=a.head  

    print("There's no way the probe could make this trip!")

    
        


if __name__ == '__main__': 
    main()
