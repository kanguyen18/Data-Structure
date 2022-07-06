import os.path
import sys
import dynamic_array as da
import argparse
import myDataStructures as ds

def populated_queue(my_queue):
    my_queue = ds.Queue()
    for i in range(my_array.__len__()):
        my_queue.enqueue(my_array[i])
    return my_queue

def is_palindrome(my_queue):
    a = my_queue.length()
    my_queue_2 = ds.Queue()
    my_stack_2 = ds.Stack()
    if a%2 == 0:
        c = int(a/2)
        for i in range(c):
            my_queue_2.enqueue(my_queue.dequeue())
        for i in range(c):
            my_stack_2.push(my_queue.dequeue())
        for i in range(c):
            if my_stack_2.pop() == my_queue_2.dequeue():
                continue
            else:
                return False
        return True
    else:
        b = int((a-1)/2)
        for i in range(b):
            my_queue_2.enqueue(my_queue.dequeue())
        c = my_queue.dequeue()
        for i in range(b):
            my_stack_2.push(my_queue.dequeue())
        for i in range(b):
            if my_stack_2.pop() == my_queue_2.dequeue():
                continue
            else:
                return False
        return True

def reverse(my_queue):
    my_stack = ds.Stack()
    reverse_queue = ds.Queue()
    for i in range(my_queue.length()):
        my_stack.push(my_queue.dequeue())
    for i in range(my_stack.length()):
        reverse_queue.enqueue(my_stack.pop())
    return reverse_queue

def count_and_sum(my_queue):
    count = 0
    sum_queue = 0
    for i in range(my_queue.length()):
        sum_queue += my_queue.dequeue()
        count += 1
    return count,sum_queue


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
        
    main_queue = populated_queue(my_array)
    copy_b = populated_queue(my_array)
    print(is_palindrome(copy_b))
    copy_c = populated_queue(my_array)
    reverse_queue = reverse(copy_c)
    print(is_palindrome(reverse_queue))
    copy_d = populated_queue(my_array)
    reverse_queue = reverse(copy_d)
    print(reverse_queue.front())
    print(count_and_sum(main_queue))
        
    