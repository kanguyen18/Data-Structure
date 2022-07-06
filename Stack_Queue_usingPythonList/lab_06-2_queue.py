import os.path
import argparse
import copy

class Stack:
    def __init__(self):
        self._stack = []
        self._tail = -1
    
    def push(self,value):
        self._stack.append(value)
        self._tail += 1
        
    def is_empty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False
        
    def top(self):
        if self.is_empty():
            raise ValueError("The stack is empty.")
        else:
            return self._stack[self._tail]
        
    def pop(self):
        if len(self._stack) == 0:
            raise ValueError("Nothing to pop")
        else:
            return self._stack.pop()

class Queue:
    def __init__(self):
        self._queue = []
     
    def is_empty(self):
        if len(self._queue) == 0:
            return True
        else:
            return False
            
    def enqueue(self,value):
        self._queue.append(value)
        
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Nothing to dequeue")
        else:
            dequeue_value = self._queue[0]
            del self._queue[0]
            return dequeue_value
        
    def front(self):
        return self._queue[0]

def populated_queue(input_file):
    my_queue = Queue()
    for i in input_file:
        i = int(i.strip('\n'))
        my_queue.enqueue(i)
    return my_queue

def is_palindrome(my_queue):
    a = 0
    my_queue_2 = Queue()
    while my_queue.is_empty() == False:
        my_queue_2.enqueue(my_queue.dequeue())
        a += 1
        
    my_stack_2 = Stack()
    if a%2 == 0:
        for i in range(a//2):
            my_stack_2.push(my_queue_2.dequeue())
        for i in range(a//2):
            if my_stack_2.pop() == my_queue_2.dequeue():
                continue
            else:
                return False
        return True
    else:
        for i in range(a//2):
            my_stack_2.push(my_queue_2.dequeue())
        my_queue_2.dequeue()
        for i in range(a//2):
            if my_stack_2.pop() == my_queue_2.dequeue():
                continue
            else:
                return False
        return True

def reverse(my_queue):
    my_stack = Stack()
    reverse_queue = Queue()
    while my_queue.is_empty() == False:
        my_stack.push(my_queue.dequeue())
    while my_stack.is_empty() == False:
        reverse_queue.enqueue(my_stack.pop())
    return reverse_queue

def count_and_sum(my_queue):
    count = 0
    sum_queue = 0
    while my_queue.is_empty() == False:
        sum_queue += my_queue.dequeue()
        count += 1
    return count,sum_queue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 6 part 2')
    parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
        
    my_queue = populated_queue(input_file)
    queue_copy_b = copy.deepcopy(my_queue)
    print(is_palindrome(queue_copy_b))
    queue_copy_c = copy.deepcopy(my_queue)
    reverse_queue = reverse(queue_copy_c)
    copy_reverse = copy.deepcopy(reverse_queue)
    print(is_palindrome(copy_reverse))
    print(reverse_queue.front())
    print(count_and_sum(my_queue))
