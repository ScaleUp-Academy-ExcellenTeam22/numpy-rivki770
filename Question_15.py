import numpy as np


def three_dimension_array():
    '''
    The function create a three-dimension array.
    :return: Nothing.
    '''
    # np.random.seed(32)
    array_3D = np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
    print(array_3D)


if __name__ == '__main__':
    three_dimension_array()
