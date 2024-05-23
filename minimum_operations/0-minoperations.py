#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    if n <= 1:
        return 0
    num_of_operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:  # If n is even
            n = n / divisor
            num_of_operations = num_of_operations + divisor
        else:
            divisor += 1

    return num_of_operations
