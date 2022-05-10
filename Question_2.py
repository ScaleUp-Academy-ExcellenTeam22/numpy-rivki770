import numpy as np


def changing_linspace():
    '''
    The function create vector of length 10 with values evenly distributed between 5 and 50.
    :return: nothing.
    '''
    v = np.linspace(10, 49, 5)
    print("Vector of length 10 with values evenly distributed between 5 and 50:")
    print(v)


if __name__ == '__main__':
    changing_linspace()
