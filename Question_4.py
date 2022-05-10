import numpy as np


def change_element_in_inside(matrix):
    '''
    The function change the element in inside to 0.
    :param matrix: The matrix with value one
    :return: nothing.
    '''
    matrix[1:-1, 1:-1] = 0
    print('\nThe matrix after change:')
    print(matrix)


def create_matrix_one():
    '''
    The function create matrix with value one.
    :return: the matrix.
    '''
    matrix_one = np.ones((10, 10))
    print('The matrix:')
    print(matrix_one)
    return matrix_one


def main():
    change_element_in_inside(create_matrix_one())


if __name__ == '__main__':
    main()
