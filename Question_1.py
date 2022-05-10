import numpy as np


def changing_sign():
    '''
    The function create list of numbers between 0-20 and changing the sign of the numbers in the range from 9 to 15.
    :return: nothing.
    '''
    list_numbers = np.arange(21)
    print("Before change the sign of the numbers:")
    print(list_numbers)
    print("After changing the sign of the numbers in the range from 9 to 15:")
    list_numbers[(list_numbers >= 9) & (list_numbers <= 15)] *= -1
    print(list_numbers)


if __name__ == '__main__':
    changing_sign()
