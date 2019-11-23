import random

def comb_sort(array):
    ''' Comb sort uses gap > 1, where bubble sort fixes gap size = 1.
        Start with gap size = len(array) // 1.3, 
        then keep shrinking by 1.3 until gap size reaches 1.

        Once gap size 1 is reached, continue using gap size 1 until the list is completely sorted.

        :param array: the python list being sorted
    '''
    pass


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    comb_sort(array)
    print("After sorting:")
    print(array)

if __name__ == '__main__':
    main()