import numpy as np


def find_row_column_of_matrix(matrix):
    '''
    The function find the number of rows and columns of the matrix.
    :param matrix: The matrix.
    :return: nothing.
    '''
    print("\nNumber of rows and columns of the matrix:")
    print(matrix.shape)


def main():
    matrix = np.arange(1, 21).reshape((4, 5))  # create the matrix.
    print("The matrix:")
    print(matrix)
    find_row_column_of_matrix(matrix)


if __name__ == '__main__':
    main()
