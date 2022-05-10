import numpy as np
import matplotlib.pyplot as plt


def create_sin_graph():
    '''
    The function create the sin graph.
    :return: nothing.
    '''
    x = np.arange(0, 3 * np.pi, 0.2)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x, y)
    # plt.show() ->  not working for me.
    fig.savefig("Question6.png")  # save the picture.


if __name__ == '__main__':
    create_sin_graph()
