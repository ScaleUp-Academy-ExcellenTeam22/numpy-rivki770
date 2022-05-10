import numpy as np


def multiply_arrays(array_nums1, array_nums2):
    '''
    The function multiply arrays of same size element-by-element.
    :param array_nums1: first array.
    :param array_nums2: second array.
    :return: Nothing.
    '''
    print("\nMultiply arrays of same size element-by-element:")
    print(np.multiply(array_nums1, array_nums2))


def main():
    array_nums1 = np.array([[2, 5, 2], [1, 5, 5]])
    array_nums2 = np.array([[5, 3, 4], [3, 2, 5]])
    print(f"Array 1:\n{array_nums1}")
    print(f"Array 2:\n{array_nums2}")
    multiply_arrays(array_nums1, array_nums2)


if __name__ == '__main__':
    main()
