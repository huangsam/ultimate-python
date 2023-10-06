"""
Bitwise operators in Python allow you to manipulate individual bits of integers.
This module demonstrates the use of bitwise operators and their behavior.
"""


def main():
    # Define some integer values for demonstration
    a = 5   # Binary: 0101
    b = 3   # Binary: 0011

    # Bitwise AND (&) operator compares each bit of two integers and returns 1
    # if both bits are 1, otherwise returns 0
    result_and = a & b  # Binary: 0001 (Decimal: 1)
    assert result_and == 1

    # Bitwise OR (|) operator compares each bit of two integers and returns 1
    # if at least one bit is 1, otherwise returns 0
    result_or = a | b  # Binary: 0111 (Decimal: 7)
    assert result_or == 7

    # Bitwise XOR (^) operator compares each bit of two integers and returns 1
    # if the bits are different (one is 1 and the other is 0), otherwise returns 0
    result_xor = a ^ b  # Binary: 0110 (Decimal: 6)
    assert result_xor == 6

    # Bitwise NOT (~) operator inverts all bits of an integer
    # It return the one's complement of the integer
    result_not_a = ~a  # Binary: 11111010 (Decimal: -6)
    assert result_not_a == -6

    # Bitwise left shift (<<) operator shifts the bits of an integer to the left by 
    # a specified number of positions, filling with zeros
    result_left_shift = a << 2  # Binary: 010100 (Decimal: 20)
    assert result_left_shift == 20

    # Bitwise right shift (>>) operator shifts the bits of an integer to the right
    # by a specified number of positions, filling with zeros for positive numbers
    # and with ones for negative numbers
    result_right_shift = a >> 1  # Binary: 0010 (Decimal: 2)
    assert result_right_shift == 2


if __name__ == "__main__":
    main()
