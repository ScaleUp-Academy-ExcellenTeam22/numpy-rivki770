import numpy as np


def remove_single_dimensional_entries(shape):
    '''
    The function remove single-dimensional entries from a specified shape.
    :param shape: specified shape.
    :return: Nothing.
    '''
    print(np.squeeze(shape).shape)


def main():
    shape = np.zeros((3, 1, 4))
    remove_single_dimensional_entries(shape)


if __name__ == '__main__':
    main()

