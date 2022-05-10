import numpy as np


def swapping_between_rows(arr_numbers):
    '''
    The function swapping between row last and first.
    :param arr_numbers: array of numbers.
    :return: Nothing.
    '''
    new_arr_numbers = arr_numbers[::-1]
    print(f"\nNew array after swapping first and last rows of the said array:\n{new_arr_numbers}")


def create_array():
    '''
    The function create array 4*4.
    :return: the array.
    '''
    arr_numbers = np.arange(16, dtype='int').reshape(-1, 4)
    print(f"Original array:\n{arr_numbers}")
    return arr_numbers


def main():
    swapping_between_rows(create_array())


if __name__ == '__main__':
    main()
