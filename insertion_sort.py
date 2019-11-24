import random


def insertion_sort(array):
    """ Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. 
        :param array: the python list being sorted
    """
    # To do
    if len(array) == 1:
        return array
    for i in range(len(array) - 1):
        count = i + 1
        while array[count] < array[count - 1] and count > 0:
            array[count], array[count - 1] = array[count - 1], array[count]
            count -= 1
    return array

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    insertion_sort(array)
    print("After sorting:")
    print(array)

if __name__ == '__main__':
    main()
