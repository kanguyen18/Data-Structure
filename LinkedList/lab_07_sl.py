
import os.path
import argparse
import sys

class singleLink:
    
    class _Node:   
         
        __slot__ = '_domainName', '_count', '_pointer'
        
        
        def __init__(self, domainName, pointer):
            self._domainName = domainName
            self._count = 1
            self._pointer = pointer
            
        def getDomain(self):
            return self._domainName
        
        def getCount(self):
            return self._count
        
        def incrementCount(self):
            self._count += 1
            
        def nextNode(self):
            return self._pointer   
        
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None
        
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
        
    def length(self):
        return self._size
    
    def getHead(self):
        return self._head
        
    def insertLast(self,domainName):
        # add a new Node to the end
        newNode = self._Node(domainName, None)
        if self.is_empty():
            self._head = newNode
        else:
            self._tail._pointer = newNode
        self._tail = newNode
        self._size += 1
    
def populate(input_file):
    #A method????
    myList = singleLink()
    for i in input_file:
        i = i.split(":")[0]
        current = myList.getHead()
        while current:
            if i != current.getDomain():
                current = current.nextNode()
            else:
                current.incrementCount()
                break
        if current == None:
            myList.insertLast(i)
    return myList
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 7')
    parser.add_argument('-i','--inputFileName', type=str, help='File of strings, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r') 
    myList = populate(input_file)
    totalCount = 0
    totalDomain = 0
    current = myList.getHead()
    maxName = current.getDomain()
    maxCount = current.getCount()
    
    while current:
        totalCount += current.getCount()
        totalDomain += 1
        if current.getCount() > maxCount:
            maxName = current.getDomain()
            maxCount = current.getCount()
        current = current.nextNode()
        
    print(totalCount)
    print(totalDomain)
    print(maxName + " " + str(maxCount))
    print(str(round((maxCount/totalCount)*100))+"%")
    
        
        
        
        
        
        
        
        
    