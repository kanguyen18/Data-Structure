import os.path
import argparse
import sys

class PriorityQueue:
    
    class _Item:
        
        __slot__ = '_name', '_priority'
        
        def __init__(self, name, priority, pointer = None):
            self._name = name
            self._priority = priority
            self._pointer = pointer

        def getName(self):
            return self._name

        def getPriority(self):
            return self._priority
        
        def getNext(self):
            return self._pointer
        
        def setPointer(self, pointer):
            self._pointer = pointer
         
        
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def getHead(self):
        if self.is_empty():
            raise ValueError('Empty queue.')
        else:
            return self._head.getName()
        
    def getTail(self):
        if self.is_empty():
            raise ValueError('Empty queue.')
        else:
            return self._tail.getName()
        
    def removeHead(self):
        if self.is_empty():
            raise ValueError('Empty queue.')
        else:
            if self._size == 1:
                oldHead = self._head
                newHead = self._head.getNext()
                self._head = newHead
                self._tail = self._head
                self._size -= 1
            else:    
                oldHead = self._head
                newHead = self._head.getNext()
                self._head = newHead
                self._size -= 1
            return oldHead
        
    def appropriateAdd(self, name, priority):
        if self.is_empty():
            self._head = self._Item(name, priority)
            self._tail = self._head
            self._size += 1
        else:
            if priority > self._head.getPriority():
                newHead = self._Item(name, priority, self._head)
                self._head = newHead
                self._size += 1
            else:
                current = self._head
                while current:
                    if priority < current.getPriority() or priority == current.getPriority():
                        before = current
                        current = current.getNext()
                    else:
                        newItem = self._Item(name, priority, current)
                        before.setPointer(newItem)
                        self._size += 1
                        break
                if current == None:
                    newItem = self._Item(name, priority)
                    before.setPointer(newItem)
                    self._tail = newItem
                    self._size += 1
                    
def populate2(input_file):
    priorityQueue = PriorityQueue()
    for i in input_file:
        i = i.strip('\n')
        a = i.split(', ')
        if a[0] == 'arrive':
            priorityQueue.appropriateAdd(a[1], int(a[2]))
        if a[0] == 'service':
            if priorityQueue.is_empty():
                raise ValueError("No one to serve!")
            else:
                priorityQueue.removeHead()
    return priorityQueue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 7')
    parser.add_argument('-i','--inputFileName', type=str, help='File of strings, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r') 
    
    myQueue = populate2(input_file)
    print(myQueue.getHead())
    print(myQueue.getTail())
        
        
        
        