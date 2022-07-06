import os.path
import argparse
import copy

class Deque:
    def __init__(self):
        self._deque = []
        self._back = -1
     
    def is_empty(self):
        if len(self._deque) == 0:
            return True
        else:
            return False
            
    def enqueueFront(self,value):
        self._deque.insert(0,value)
        self._back += 1
    
    def enqueueBack(self,value):
        self._deque.append(value)
        self._back += 1
        
    def dequeueFront(self):
        if self.is_empty():
            raise ValueError("Nothing to dequeue")
        else:
            dequeue_value = self._deque[0]
            del self._deque[0]
            return dequeue_value
        
    def dequeueBack(self):
        if self.is_empty():
            raise ValueError("Nothing to dequeue")
        else:
            return self._deque.pop()
        
    def front(self):
        return self._deque[0]
    
    def back(self):
        return self._deque[self._back]
    
    def length(self):
        return len(self._deque)
    
def populated_deque(input_file):
    my_deque = Deque()
    for i in input_file:
        i = int(i.strip("\n"))
        my_deque.enqueueBack(i)
    return my_deque

def is_palindrome(my_deque):
    while my_deque.length() > 1:
        if my_deque.dequeueFront() == my_deque.dequeueBack():
            continue
        else:
            return False
    return True

def reverse(my_deque):
    reverse_deque = Deque()
    while my_deque.is_empty() == False:
        reverse_deque.enqueueBack(my_deque.dequeueBack())
    return reverse_deque

def count_and_sum(my_deque):
    count = 0
    sum_deque = 0
    while my_deque.is_empty() == False:
        sum_deque += my_deque.dequeueBack()
        count += 1
    return count,sum_deque
                        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 6 part 2')
    parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
                        
    my_deque = populated_deque(input_file)
    deque_copy_b = copy.deepcopy(my_deque)
    print(is_palindrome(deque_copy_b))
    deque_copy_c = copy.deepcopy(my_deque)
    reverse_deque = reverse(deque_copy_c)
    copy_reverse = copy.deepcopy(reverse_deque)
    print(is_palindrome(copy_reverse))
    print(reverse_deque.front())
    print(count_and_sum(my_deque))
                           