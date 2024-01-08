#!/usr/bin/python3
"""Defines matrix_divided function"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix

    Args:
        matrix (list): list of lists of int or float
        div (int/float): divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns: new matrix its element rounded to 2
    """
    if (matrix == [] or not isinstance(matrix, list) or
       not all(isinstance(matrix[i], list) for i in range(len(matrix))) or
       not all((isinstance(val, int) or isinstance(val, float))
               for val in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the"
                            " same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [list(map(lambda x: round(x / div, 2), elem))
                  for elem in matrix]
    return new_matrix
