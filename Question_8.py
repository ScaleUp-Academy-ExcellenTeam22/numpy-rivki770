import numpy as np


def switch_equals(array_numbers, given_number, number_to_replace):
    '''
    The function Replace elements of the array which are equal to given_number with number_to_replace.
    :param array_numbers: The array of numbers.
    :param given_number: The number for comparison.
    :param number_to_replace: The number to replace.
    :return: Nothing.
    '''
    print("\nReplace elements of the array which are equal to ", given_number, "with", number_to_replace)
    print(np.where(array_numbers == given_number, number_to_replace, array_numbers))


def switch_greater(array_numbers, given_number, number_to_replace):
    '''
    The function Replace elements of the array which are greater to given_number with number_to_replace.
    :param array_numbers: The array of numbers.
    :param given_number: The number for comparison.
    :param number_to_replace: The number to replace.
    :return: Nothing.
    '''
    print("\nReplace elements of the array which are greater to ", given_number,"with", number_to_replace)
    print(np.where(array_numbers > given_number, number_to_replace, array_numbers))


def switch_less(array_numbers, given_number, number_to_replace):
    '''
    The function Replace elements of the array which are less to given_number with number_to_replace.
    :param array_numbers: The array of numbers.
    :param given_number: The number for comparison.
    :param number_to_replace: The number to replace.
    :return: Nothing.
    '''
    print("\nReplace elements of the array which are less to ",given_number, "with", number_to_replace)
    print(np.where(array_numbers < given_number, number_to_replace, array_numbers))


def create_array():
    '''
    The function create array.
    :return: the array.
    '''
    array_numbers = np.array([[5, 3, 7], [3, 8, 6], [1, 2, 9]])
    print(f"Original array:\n{array_numbers}")
    return array_numbers


def main():
    array_numbers = create_array()
    given_number = 3
    number_to_replace = 14
    switch_equals(array_numbers, given_number, number_to_replace)
    switch_greater(array_numbers, given_number, number_to_replace)
    switch_less(array_numbers, given_number, number_to_replace)


if __name__ == '__main__':
    main()
