import os.path
import argparse
import sys

class BinarySearchTree:  
    class _Node:   
         
        __slot__ = '_domainName', '_count', '_left', '_right', '_parent'
        
        def __init__(self, domainName, left = None, right = None, parent = None):
            self._domainName = domainName
            self._count = 1
            self._left = left
            self._right = right
            self._parent = parent
            
        def getDomain(self):
            return self._domainName
        
        def getCount(self):
            return self._count
        
        def incrementCount(self):
            self._count += 1
            
        def getLeft(self):
            return self._left
        
        def getRight(self):
            return self._right
        
        def getParent(self):
            return self._parent
        
    def __init__(self):
        self._root = None
        #self._height = 0
        self._size = 0
        
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def addRoot(self, domain):
        #if self.is_empty() == True:
        root = self._Node(domain)
        self._root = root
        self._size += 1
        #else:
            #raise ValueError("There exists a root already!")
            
    def getRoot(self):
        return self._root
        
    def appropriateAdd(self, domain, subRoot = None):
        if self.is_empty():
            self.addRoot(domain)
        else:
            if subRoot == None:
                subRoot = self._root
        
            if domain == subRoot.getDomain():
                subRoot.incrementCount()

            elif domain > subRoot.getDomain():
            #check again
                a = subRoot.getRight()
                if a == None:
                    newNode = self._Node(domain)
                    subRoot._right = newNode
                    self._size += 1
                else:
                    self.appropriateAdd(domain,a)

            elif domain < subRoot.getDomain():
                a = subRoot.getLeft()
                if a == None:
                    newNode = self._Node(domain)
                    subRoot._left = newNode
                    self._size += 1
                else:
                    self.appropriateAdd(domain,a)
                    
    def printTree(self, subRoot):
        if subRoot != None:
            self.printTree(subRoot.getLeft())
            print(subRoot.getDomain(),":",subRoot.getCount())
            self.printTree(subRoot.getRight())
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 8')
    parser.add_argument('-i','--inputFileName', type=str, help='File of strings, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
    
    myTree = BinarySearchTree()
    for i in input_file:
        i = i.split(":")[0]
        myTree.appropriateAdd(i)
    
    a = myTree.getRoot()
    myTree.printTree(a)
        
        
        
        