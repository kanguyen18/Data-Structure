import dynamic_array as da
class Stack:
    def __init__(self):
        self._stack = da.DynamicArray()
        self._tail = -1
    
    def push(self,value):
        self._stack.append(value)
        self._tail += 1
        
    def is_empty(self):
        if self._stack.__len__() == 0:
            return True
        else:
            return False
        
    def top(self):
        if self.is_empty():
            raise ValueError("The stack is empty.")
        else:
            return self._stack[self._tail]
        
    def pop(self):
        if self._stack.__len__() == 0:
            raise ValueError("Nothing to pop")
        else:
            pop_value = self._stack[self._tail]
            self._stack.remove_end()
            self._tail -= 1
            return pop_value
        
    def length(self):
        return self._stack.__len__()
                                   
    
class Queue:
#I built this class using Circular Array based on the idea in the book
    def __init__(self):
        self._queue = da.DynamicArray()
        self._n = 0
        self._capacity = 1
        self._front = 0
     
    def is_empty(self):
        if self._n == 0:
            return True
        else:
            return False
            
    def enqueue(self,value):
        if self._n == self._capacity:
            self._queue.reorder(self._front)
            self._queue.append(value)
            self._front = 0
            self._n += 1
            self._capacity = self._capacity*2
        else:
            avail = (self._front + self._n) % self._capacity
            self._queue.replace_index(avail,value)
            self._n += 1
        
    def dequeue(self):
        if self.is_empty():
            raise("Nothing to dequeue")
        else:
            dequeue_value = self._queue[self._front]
            self._front = (self._front + 1) % self._capacity
            self._n -= 1
            return dequeue_value
        
    def front(self):
        return self._queue[self._front]
        
    def length(self):
        return self._n    

class Deque:
    def __init__(self):
        self._deque = da.DynamicArray()
        self._n = 0
        self._capacity = 1
        self._front = 0
     
    def is_empty(self):
        if self._n == 0:
            return True
        else:
            return False
            
    def enqueue(self,value):
        if self._n == self._capacity:
            self._queue.reorder(self._front)
            self._queue.append(value)
            self._front = 0
            self._n += 1
            self._capacity = self._capacity*2
        else:
            avail = (self._front + self._n) % self._capacity
            self._queue.replace_index(avail,value)
            self._n += 1
        
    def dequeue(self):
        if self.is_empty():
            raise("Nothing to dequeue")
        else:
            dequeue_value = self._queue[self._front]
            self._front = (self._front + 1) % self._capacity
            self._n -= 1
            return dequeue_value
        
    def front(self):
        return self._queue[self._front]
        
    def length(self):
        return self._n    
            
            
        
        
        
        
        