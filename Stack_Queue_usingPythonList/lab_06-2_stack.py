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
        
def populated_stack(input_file):
    my_stack = Stack()
    for i in input_file:
        i = int(i.strip('\n'))
        my_stack.push(i)
    return my_stack


def is_palindrome(my_stack):
    a = 0
    my_stack_2 = Stack()            
    while my_stack.is_empty() == False:
        my_stack_2.push(my_stack.pop())
        a += 1
    my_stack_3 = Stack()
    if a%2 == 0:
        for i in range(a//2):
            my_stack_3.push(my_stack_2.pop())
        for i in range(a//2):
            if my_stack_2.pop() == my_stack_3.pop():
                continue
            else:
                return False
        return True
    else:
        for i in range(a//2):
            my_stack_3.push(my_stack_2.pop())
        my_stack_2.pop()
        for i in range(a//2):
            if my_stack_2.pop() == my_stack_3.pop():
                continue
            else:
                return False
        return True
            
def reverse(my_stack):
    reverse_stack = Stack()
    while my_stack.is_empty() == False:
        reverse_stack.push(my_stack.pop())
    return reverse_stack
        
    
def count_and_sum(my_stack):
    count = 0
    sum_stack = 0
    while my_stack.is_empty() == False:
        sum_stack += my_stack.pop()
        count += 1
    return count,sum_stack


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lab 6 part 2')
    parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)
        
    input_file = open(args.inputFileName,'r')
       
    my_stack = populated_stack(input_file)
    stack_copy_b = copy.deepcopy(my_stack)
    print(is_palindrome(stack_copy_b))
    stack_copy_c = copy.deepcopy(my_stack)
    reverse_stack = reverse(stack_copy_c)
    copy_reverse = copy.deepcopy(reverse_stack)
    print(is_palindrome(copy_reverse))
    print(reverse_stack.top())
    print(count_and_sum(my_stack))
              
                