import numpy as np


def combine_array_and_matrix(array, matrix):
    '''
    The function combines a one-dimensional and two-dimensional array and display their elements.
    :param array: one dimensional array.
    :param matrix: two dimensional array.
    :return: Nothing.
    '''
    for element_array, element_matrix in np.nditer([array, matrix]):
        print("%d:%d" % (element_array, element_matrix),)


def main():
    array = np.arange(4)
    print(f"The array:\n{array}")
    matrix = np.arange(8).reshape(2, 4)
    print(f"The matrix:\n{matrix}")
    print(f"\nThe combine:")
    combine_array_and_matrix(array, matrix)


if __name__ == '__main__':
    main()
