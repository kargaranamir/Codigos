class Queue:

    def __init__(self):
        self.queue = list()
        
    def __iter__(self):
        return self.queue
    
    def enqueue(self,data):
        self.queue.append(data)


    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("Queue Empty!")

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue
    
    def __getitem__(self, key):
        return self.queue[key]
    
def fifo(a,n,capacity):
    f = -1
    page_faults = 0
    page = Queue()
    for i in range(capacity):
        page.enqueue(-1)
    for i in range(n):
        flag = 0
        for j in range(capacity):
            if(page.__getitem__(j) == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%capacity
            page.__iter__()[f]=a[i]
            page_faults+=1
            
    print (str(page_faults))


def main():
    capacity = int(input())
    a = list(map(int,input().strip().split()))
    n=len(a)
    fifo(a,n,capacity)


if __name__ == '__main__': 
    main()

