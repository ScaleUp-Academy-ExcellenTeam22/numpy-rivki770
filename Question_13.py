import numpy as np


def two_array_to_matrix(array_one, array_two):
    '''
    The function convert two 1-D arrays into a 2-D array.
    :param array_one: array number 1.
    :param array_two: array number 2.
    :return: Nothing.
    '''
    matrix = np.dstack((array_one, array_two))
    print(matrix)


def main():
    array_one = np.array([[10], [20], [30]])
    array_two = np.array([[40], [50], [60]])
    two_array_to_matrix(array_one, array_two)


if __name__ == '__main__':
    main()
