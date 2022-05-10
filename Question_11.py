import numpy as np


def unit_matrix_3D():
    '''
    The function create a 3-D array with ones on the diagonal and zeros elsewhere.
    :return: Nothing
    '''
    unit_matrix = np.eye(3)
    print(unit_matrix)


if __name__ == '__main__':
    unit_matrix_3D()
