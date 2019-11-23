import random

def merge(temp_array1, temp_array2, array):
    """ Merge two sorted lists temp_array1 and temp_array2 into properly sized list S.

        (This is the merge step, merge two sorted lists.)
        
        :param temp_array1: left half array copy
        :param temp_array2: right half array copy
        :param array:       the original array being sorted
    """
    # To do
    pass
    

def merge_sort(array):
    """ Sort the elements of Python list using the merge-sort algorithm.
        :param array: the original array being sorted
    """
    # To do
    pass

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    merge_sort(array)
    print("After sorting:")
    print(array)

if __name__ == '__main__':
    main()








