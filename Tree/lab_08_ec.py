import os.path
import argparse
import sys
import lab_08 as bst

class BSTcount:
    class _Node:   
         
        __slot__ = '_domainName', '_count', '_left', '_right', '_parent'
        
        def __init__(self, domainName, count = 1, left = None, right = None, parent = None):
            self._domainName = domainName
            self._count = count
            self._left = left
            self._right = right
            self._parent = parent
            
        def getDomain(self):
            return self._domainName
        
        def getCount(self):
            return self._count
            
        def getLeft(self):
            return self._left
        
        def getRight(self):
            return self._right
        
        def getParent(self):
            return self._parent

    def __init__(self):
        self._root = None
        self._size = 0
        
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def addRoot(self, domain):
        if self.is_empty() == True:
            root = self._Node(domain)
            self._root = root
            self._size += 1
        else:
            raise ValueError("There exists a root already!")
            
    def getRoot(self):
        return self._root
    
    def approAdd(self, node, subRoot = None):
        if self.is_empty():
            self._root = self._Node(node.getDomain(),node.getCount())
            self._size += 1
        else:
            if subRoot == None:
                subRoot = self._root
            # Take care of the special (base) case before using recursive 
            
            if node.getCount() == subRoot.getCount():
            # In the case of equivalent count, I use the domain name to compare    
                if node.getDomain() > subRoot.getDomain():
                    a = subRoot.getRight()
                    # I use variable a so I can still keep the pointers of the subroot
                    if a == None:
                        newNode = self._Node(node.getDomain(),node.getCount())
                        subRoot._right = newNode
                        self._size += 1
                    else:
                        self.approAdd(node,a)
                
                if node.getDomain() < subRoot.getDomain():
                    a = subRoot.getLeft()
                    if a == None:
                        newNode = self._Node(node.getDomain(),node.getCount())
                        subRoot._left = newNode
                        self._size += 1
                    else:
                        self.approAdd(node,a)
                    
            elif node.getCount() > subRoot.getCount():
                a = subRoot.getRight()
                if a == None:
                    newNode = self._Node(node.getDomain(),node.getCount())
                    subRoot._right = newNode
                    self._size += 1
                else:
                    self.approAdd(node,a)

            elif node.getCount() < subRoot.getCount():
                a = subRoot.getLeft()
                if a == None:
                    newNode = self._Node(node.getDomain(),node.getCount())
                    subRoot._left = newNode
                    self._size += 1
                else:
                    self.approAdd(node,a)
        
    
    def populate(self, current):
        #current is the old tree's root
        if current != None:
            self.approAdd(current)
            self.populate(current.getLeft())
            self.populate(current.getRight())
    
    def printTree(self, subRoot):
        if subRoot != None:
            self.printTree(subRoot.getLeft())
            print(subRoot.getCount(),":",subRoot.getDomain())
            self.printTree(subRoot.getRight())
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 8')
    parser.add_argument('-i','--inputFileName', type=str, help='File of strings, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
    
    myTree = bst.BinarySearchTree()
    for i in input_file:
        i = i.split(":")[0]
        myTree.appropriateAdd(i)
       
    treeCount = BSTcount()
    treeCount.populate(myTree.getRoot())
    treeCount.printTree(treeCount.getRoot())
    
        
        