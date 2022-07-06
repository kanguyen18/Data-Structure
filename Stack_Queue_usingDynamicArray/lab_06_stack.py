import os.path
import sys
import dynamic_array as da
import argparse
import myDataStructures as ds


def populated_stack(my_array):
    my_stack = ds.Stack()
    for i in range(my_array.__len__()):
        my_stack.push(my_array[i])
    return my_stack

# cannot make deep copy here since we can go over every element of a stack without changing the stack
# make deep copy in Stack class
    

def is_palindrome(my_stack):
    a = my_stack.length()
    my_stack_2 = ds.Stack()
    if a%2 == 0:
        c = int(a/2)
        for i in range(c):
            my_stack_2.push(my_stack.pop())
        for i in range(c):
            if my_stack_2.pop() == my_stack.pop():
                continue
            else:
                return False
        return True
    else:
        b = int((a-1)/2)
        for i in range(b):
            my_stack_2.push(my_stack.pop())
        c = my_stack.pop()
        for i in range(b):
            if my_stack_2.pop() == my_stack.pop():
                continue
            else:
                return False
        return True
        
            
def reverse(my_stack):
    reverse_stack = ds.Stack()
    for i in range(my_stack.length()):
        reverse_stack.push(my_stack.pop())
    return reverse_stack
        
    
def count_and_sum(my_stack):
    count = 0
    sum_stack = 0
    for i in range(my_stack.length()):
        #a = my_stack.pop()
        sum_stack += my_stack.pop()
        count += 1
    return count,sum_stack


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Stack')
    parser.add_argument('-i','--file_name', type=str, help='File of integers')
    args = parser.parse_args()

    if os.path.isfile(args.file_name):
        input_file = open(args.file_name,'r')
    else:
        raise ValueError("The file doesn't exist!")
       
    my_array = da.DynamicArray()
    for i in input_file:
        i = i.strip('\n')
        my_array.append(int(i))
    
    main_stack = populated_stack(my_array)
    copy_b = populated_stack(my_array)
    print(is_palindrome(copy_b))
    copy_c = populated_stack(my_array)
    reverse_stack = reverse(copy_c)
    print(is_palindrome(reverse_stack))
    copy_d = populated_stack(my_array)
    reverse_stack = reverse(copy_d)
    print(reverse_stack.top())
    print(count_and_sum(main_stack))