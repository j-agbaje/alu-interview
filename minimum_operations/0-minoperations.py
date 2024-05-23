#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """ Minimum Operations needed to get n H characters """
    y = int(n)  # n at the start of the function
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

    return f"Min number of operations to reach {y} characters: {num_of_operations}"
