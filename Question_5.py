import numpy as np


def add_vector_to_matrix(vector, matrix):
    '''
    The function add a vector to each row of a given matrix.
    :param vector: The vector.
    :param matrix: The matrix.
    :return: nothing
    '''
    for i in range(matrix.shape[0]):  # move on the row.
        matrix[i, :] = matrix[i, :] + vector
    print(f"\nAfter adding the vector to each row of the matrix:\n{matrix}")


def main():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # Create matrix.
    print(f"Original matrix:\n{matrix}")
    vector = np.array([1, 0, 1])  # Create vector.
    print(f"Original vector:\n{vector}")
    add_vector_to_matrix(vector, matrix)


if __name__ == '__main__':
    main()
