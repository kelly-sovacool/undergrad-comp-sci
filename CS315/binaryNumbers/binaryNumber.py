#!/usr/local/bin/python3
"""
CS315 Homework 4 through 6: Binary numbers and arithmetic
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Date: 21 Sept. 2017
Updated: 16 Nov. 2017
Usage:
        ./binaryNumber.py
        ./binaryNumber.py human-readable
        ./binaryNumber.py human-readable <tab-delimited_input_filename>
"""
import datetime
import math
import random
import sys
import time


class BinaryNumber(list):
    """ Represent a binary number as a list of digits, with the leftmost digit being the LEAST significant. """

    human_readable_string = False  # represent the number in human-readable form or as a list of digits

    def __init__(self, iterable=None, dec=None):
        """
        Initialize a BinaryNumber as empty list, from an iterable of integers, or from a decimal number.
        :param iterable: iterable object of zeros and ones
        :param dec: decimal number to convert to binary
        """
        if iterable:
            super().__init__(iterable)
        else:
            super().__init__()
        if dec:  # convert from decimal number
            while dec > 0:
                self.append(int(dec % 2))
                dec //= 2

    def __add__(self, other, keep_final_carry_digit=True):
        """ Addition + School method """
        result = BinaryNumber()
        carry_digit = 0
        x, y = self.equalize_length(other)
        for digitX, digitY in zip(x, y):
            new_digit = digitX + digitY + carry_digit
            if new_digit == 3:
                carry_digit = 1
                new_digit = 1
            elif new_digit == 2:
                carry_digit = 1
                new_digit = 0
            else:
                carry_digit = 0
            result.append(new_digit)
        if carry_digit and keep_final_carry_digit:
            result.append(carry_digit)
        result.check_validity()
        return result

    def __sub__(self, other):
        """ Subtraction - Two's complement method"""
        x, y = self.equalize_length(other)
        result = self.__add__(y.twos_complement, keep_final_carry_digit=False)
        result.check_validity()
        return result

    def __mul__(self, other):
        """ Multiplication * School method """
        x, y = self.equalize_length(other)
        result = BinaryNumber()
        i = 0
        for digitY in y:
            current_intermediate = BinaryNumber()
            for j in range(i):  # offset intermediate line with zeros at least significant end
                current_intermediate.append(0)
            for digitX in x:
                current_intermediate.append(digitX * digitY)
            result += current_intermediate
            i += 1
        result.check_validity()
        return result

    def __div__(self, divisor):
        """ Division / Subtraction method """
        quotient = BinaryNumber([0])
        dividend = self.copy
        while dividend >= divisor:
            dividend -= divisor
            quotient += BinaryNumber([1])
        return quotient, dividend  # dividend is now the remainder

    def __truediv__(self, other):
        """ Division / Long division """
        divisor = other
        quotient = BinaryNumber()
        remainder = BinaryNumber()
        subdividend = BinaryNumber()
        if self < divisor:
            quotient.append(0)
            remainder = self.copy
        else:
            i = len(self)
            while divisor > subdividend and i >= 0:  # get first subdividend
                i -= 1
                subdividend.insert(0, self[i])
            while i >= 0:  # iterate over digits of dividend
                temp_quotient, remainder = subdividend.__div__(divisor)
                for digit in reversed(temp_quotient):
                    quotient.insert(0, digit)
                i -= 1
                subdividend = remainder.copy
                subdividend.insert(0, self[i])
        return quotient, remainder

    def __floordiv__(self, divisor):
        """ Floor Division // """
        return (self / divisor)[0]  # discard remainder, return quotient

    def ceil_div(self, divisor):
        """ Ceiling Division """
        return (self + divisor - BinaryNumber([1])) // divisor

    def __mod__(self, other):
        """ Modulo % """
        return (self / other)[1]  # discard quotient, return remainder

    def __pow__(self, power, modulo=None):
        """ Exponentiation ** """
        z = BinaryNumber([1])
        w = self.copy
        for digit in power:
            if digit == 1:
                z = z * w % modulo if modulo else z * w
            w = w * w % modulo if modulo else w * w
        return z

    def __iadd__(self, other):
        """ In-place addition += """
        return self + other

    def __isub__(self, other):
        """ In-place subtraction += """
        return self - other

    def __imul__(self, other):
        """ In-place multiplication *= """
        return self * other

    def __idiv__(self, other):
        """ In-place division /= """
        return self / other

    def __str__(self):
        """
        If the class variable human_readable_string is True,
        the number will be represented as a string with the leftmost digit as the MOST significant.
        Otherwise, the number will be represented as a list with the leftmost digit being the LEAST significant.
        :return: String representation of the binary number.
        """
        self.remove_trailing_zeros()
        return "".join(reversed([str(d) for d in self])) if BinaryNumber.human_readable_string else super().__str__()

    def __lt__(self, other):
        """ Less than < """
        self.remove_trailing_zeros()
        other.remove_trailing_zeros()
        if len(self) == len(other):
            result = False
            for digitX, digitY in zip(reversed(self), reversed(other)):
                if digitX != digitY:  # first non-equal significant digit decides the result
                    result = digitX < digitY
                    break
        else:
            result = len(self) < len(other)
        return result

    def __le__(self, other):
        """ Less than or equal <= """
        return self < other or self == other

    def __eq__(self, other):
        """ Equal == """
        self.remove_trailing_zeros()
        other.remove_trailing_zeros()
        if len(self) == len(other):
            result = True
            for digitX, digitY in zip(self, other):
                if digitX != digitY:  # all digits must be equal
                    result = False
                    break
        else:
            result = False
        return result

    def __ne__(self, other):
        """ Not equal != """
        return not (self == other)

    def __gt__(self, other):
        """ Greater than > """
        return not (self <= other)

    def __ge__(self, other):
        """ Greater than or equal >= """
        return self == other or self > other

    @property
    def twos_complement(self):
        """ Return the two's complement of self """
        result = self.copy
        for i in range(len(result)):
            result[i] = 0 if result[i] else 1  # flip ones to zeros and zeros to ones
        return result + BinaryNumber([1])

    @property
    def copy(self):
        """ Return a shallow copy of self """
        return BinaryNumber(self)

    @property
    def split(self):
        """ Return left & right halves """
        n = len(self) / 2
        return BinaryNumber(self[:math.ceil(n)]), BinaryNumber(self[math.ceil(n):])

    @property
    def is_prime_fermat(self):
        """ Fermat's test of primality """
        return BinaryNumber([1, 1]).__pow__((self - BinaryNumber([1])), modulo=self) == (BinaryNumber([1]) % self)

    @property
    def is_prime_brute(self):
        """ Determine primality with a brute-force approach """
        decimal = self.decimal
        if decimal > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(decimal)) + 1):
                if decimal % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        return is_prime

    @property
    def decimal(self):
        """ Return self as an integer in base 10 """
        decimal = 0
        for i in range(len(self)):
            decimal += self[i] * 2 ** i
        return decimal

    def check_validity(self):
        """ Make sure all digits are integers and either zero or one. """
        for digit in self:
            if type(digit) != int:
                raise TypeError("Digit {} is not an integer for binary number {}.".format(digit, self))
            elif digit != 0 and digit != 1:
                raise ValueError("Digit {} is neither zero nor one for binary number {}".format(digit, self))

    def equalize_length(self, other):
        """
        Make sure the numbers are the same length; if needed, add zeros to the shorter number at the most significant end.
        :param other: binary number
        :return: copies of binary numbers self & other
        """
        x = self.copy
        y = other.copy
        if len(x) > len(y):
            difference = len(x) - len(y)
            for i in range(difference):
                y.append(0)
        elif len(x) < len(y):
            difference = len(y) - len(x)
            for i in range(difference):
                x.append(0)
        return x, y

    def remove_trailing_zeros(self):
        """
        Remove any zeros at the most significant end before the most significant 1.
        Doesn't check the least significant digit in case the number is zero.
        :return: None (modifies self in place)
        """
        if len(self) > 1:
            for i in range(len(self) - 1, 0, -1):
                if self[i] == 0:
                    self.pop()
                else:
                    break

    @classmethod
    def generate_random_odd(cls, number_digits):
        """
        Generate a pseudo-random odd binary number
        :param number_digits: size of the number to generate
        :return: binary number
        """
        return cls([1] + [random.randint(0, 1) for x in range(number_digits - 2)] + [1])


def hw2():
    if len(sys.argv) > 2:
        # file must be text with a pair of binary integers per line (leftmost digit = MOST significant), delimited by whitespace
        filename = sys.argv[2]
        with open(filename, 'r') as input_file:
            for line in input_file:
                split_line = line.split()
                x = BinaryNumber(reversed([int(digit) for digit in split_line[0]]))
                y = BinaryNumber(reversed([int(digit) for digit in split_line[1]]))
                hw2_print_arithmetic_results(x, y)
    else:  # manual entry
        x = BinaryNumber(reversed([int(char) for char in input("Enter x: ")]))  # input numbers with the leftmost digit as MOST significant
        y = BinaryNumber(reversed([int(char) for char in input("Enter y: ")]))
        hw2_print_arithmetic_results(x, y)


def hw2_print_arithmetic_results(x, y):
    print('x = ', x, '   y = ', y, sep='')
    print('\tx + y =', x + y)  # problem 1
    print('\tx - y =', x - y)  # problem 2
    print('\tx * y =', x * y)  # problem 3


def hw4():
    BinaryNumber.human_readable_string = True if len(sys.argv) > 1 and sys.argv[1] == 'human-readable' else False

    problem1_cases = [{'x': [0, 1, 1, 0, 0, 0, 1, 1, 1], 'y': [1, 1, 1, 1, 0, 1, 1, 0, 1]},
                      {'x': [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 'y': [0, 1, 1, 0, 1]},
                      {'x': [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], 'y': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}]
    print('\nProblem 1: Division\n')
    for test_case in problem1_cases:
        hw4_problem1(test_case)
    problem2_cases = [{'N': [0, 0, 1, 0, 1], 'x': [0, 1], 'y': [0, 1, 0, 1]},
                      {'N': [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], 'x': [1, 0, 1, 1], 'y': [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]},
                      {'N': [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 'x': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 'y': [1, 1, 0, 0, 0, 1, 1]}]
    print('\nProblem 2: Modular Exponentiation\n')
    for test_case in problem2_cases:
        hw4_problem2(test_case)
    print('\nProblem 3: Performance\n')
    hw4_problem3()


def hw4_problem1(test_case):  # run a test case for Problem 1 and report results
    x = BinaryNumber(test_case['x'])
    y = BinaryNumber(test_case['y'])
    print('x =', x, '\ty =', y)
    start = time.time()
    quotient, remainder = x / y
    seconds = time.time() - start
    print('\tQuotient =', quotient, '\tremainder =', remainder)
    print("\tRuntime:", datetime.timedelta(seconds=seconds), "(hrs:mins:secs)")
    print('---')


def hw4_problem2(test_case):  # run a test case for Problem 2 and report results
    x = BinaryNumber(test_case['x'])
    y = BinaryNumber(test_case['y'])
    N = BinaryNumber(test_case['N'])
    print('x =', x, '\ny =', y, '\nN =', N)
    start = time.time()
    mod_exp = x.__pow__(y, modulo=N)
    seconds = time.time() - start
    print('\tx^y mod N:', mod_exp)
    print("\tRuntime:", datetime.timedelta(seconds=seconds), "(hrs:mins:secs)")
    print('---')
    return seconds


def hw4_problem3():  # generate and run test cases for Problem 3 as long as runtime is less than 600 seconds
    time_limit = 600
    n = 1
    runtime = 0
    while runtime < time_limit:
        print('n =', n)
        zeros = [0] * n
        ones = [1] * n
        N = BinaryNumber([1, 0, 1] + zeros + ones + [0, 1])
        x = BinaryNumber([1, 1] + zeros + ones)
        y = BinaryNumber([1, 0] + zeros + ones)
        runtime = hw4_problem2({'N': N, 'x': x, 'y': y})
        n *= 2


def hw6():
    print('task 1: 100 random numbers')
    print('i\tbinary\tdecimal\tis_prime\tfermat')
    real_primes = 0
    false_fermats = 0
    for x in range(100):
        number = BinaryNumber.generate_random_odd(16)
        is_prime = number.is_prime_brute
        fermat = number.is_prime_fermat
        if is_prime:
            real_primes += 1
        elif fermat:
            false_fermats += 1
        print(str(x) + '\t' + str(number) + '\t' + str(number.decimal) + '\t' + str(is_prime) + '\t' + str(fermat))
    print('primes:\t' + str(real_primes))
    print('false fermat tests:\t' + str(false_fermats))

    print('\ntask 2: chance of random prime')
    print('digits\trandoms_before_prime')
    for size in (16, 32, 64):
        is_prime = False
        count = 0
        while not is_prime:
            number = BinaryNumber.generate_random_odd(size)
            is_prime = number.is_prime_brute
            count += 1
        print(str(size) + '\t' + str(count))


def main():
    BinaryNumber.human_readable_string = True if len(sys.argv) > 1 and sys.argv[1] == 'human-readable' else False
    hw2()
    hw4()
    hw6()


if __name__ == "__main__":
    main()
