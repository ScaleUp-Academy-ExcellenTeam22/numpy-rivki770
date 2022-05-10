import numpy as np


def sort_along_axis():
    '''
    The function sort an along the first, last axis of an array.
    :return: Nothing
    '''
    array_numbers = np.array([[4, 6], [2, 1]])
    print(f"Original array:\n{array_numbers}")
    print(f"Sort along the first axis:\n{np.sort(array_numbers, axis=0)}")
    print(f"Sort along the last axis:\n{np.sort(array_numbers, axis=1)}")


if __name__ == '__main__':
    sort_along_axis()
