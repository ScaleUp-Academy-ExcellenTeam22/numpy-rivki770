import numpy as np


def median_calculation(array):
    '''
    The function compute the median of flattened given array.
    :param array: array of numbers.
    :return: Nothing.
    '''
    # np.random.seed(32)
    median = np.median(array)
    print(f"\nMedian of the array:\n{median}")


def main():
    array = np.arange(12).reshape((2, 6))
    print(f"The array:\n{array}")
    median_calculation(array)


if __name__ == '__main__':
    main()

