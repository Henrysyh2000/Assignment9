import random

def bubble_sort(array):
    """ Compares each pair of adjacent items and swaps them if they are in the wrong order. 
        :param array: the python list being sorted
    """
    # Your code
    num = len(array)
    while num > 0:
        for i in range(num - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        num -= 1
    return array
def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    bubble_sort(array)
    print("After sorting:")
    print(array)

if __name__ == '__main__':
    main()