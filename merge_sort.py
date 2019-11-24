import random
def merge(temp_array1, temp_array2, array):
    """ Merge two sorted lists temp_array1 and temp_array2 into properly sized list S.

        (This is the merge step, merge two sorted lists.)
        
        :param temp_array1: left half array copy
        :param temp_array2: right half array copy
        :param array:       the original array being sorted
    """
    # To do
    res = []
    while temp_array1 and temp_array2:
        if temp_array1[0] < temp_array2[0]:
            res.append(temp_array1[0])
            temp_array1.pop(0)
        else:
            res.append(temp_array2[0])
            temp_array2.pop(0)
    res += temp_array1 + temp_array2
    return res
def merge_sort(array):
    """ Sort the elements of Python list using the merge-sort algorithm.
        :param array: the original array being sorted
    """
    # To do
    def helper(array):    
        if len(array) == 0:
            return array
        elif len(array) == 1:
            return array
        mid = len(array) // 2
        left = helper(array[:mid])
        right = helper(array[mid:])
        return merge(left, right, array)
    res = helper(array)
    for i in range(len(array)):
        array[i] = res[i]
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








