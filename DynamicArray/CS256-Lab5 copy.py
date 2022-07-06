import os.path
import dynamic_array as da
import argparse

def populated_array(input_file):
    my_array = da.DynamicArray()
    index_count = 0
    for i in input_file:
        i = i.strip('\n')
        my_array.insertEfficient(index_count,int(i))
        index_count += 1
    return my_array
        
def displayUniqueList(my_array):
    uniqueList = []
    for i in my_array:
        if not i in uniqueList:
            uniqueList.append(i)         
    for i in uniqueList:
        print(i)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Dynamic arrays')
    parser.add_argument('-i','--file_name', type=str, help='File of integers')
    args = parser.parse_args()

    if os.path.isfile(args.file_name):
        input_file = open(args.file_name,'r')
    else:
        raise ValueError("The file doesn't exist!")
        
    my_array = populated_array(input_file)
    displayUniqueList(my_array)
    
    print(my_array.__getitem__(-15))
    my_array.removeAll(7)
    print(my_array.__getitem__(-15))
    