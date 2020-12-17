""" Euclidean Theory functions

Author: Preocts <preocts@preocts.com>
"""
from typing import Tuple


def euclid_theory(num1: int, num2: int) -> int:
    """ Find the GCD of two numbers """
    remainder = (num1 % num2)
    return num2 if remainder == 0 else euclid_theory(num2, remainder)


def extended_euclid(num1: int, num2: int) -> Tuple[int, int]:
    """ Answer to Bezout's theorem through extending Euclid's theorem

    (s, t) must exist where: num1(s) + num2(t) = GCD(num1, num2)

    GCD is found with Euclidean: num1 = m(num2) + r
        where m is the multiple of num2 into num1 and r is the remainder

    """
    if num2 == 0:
        return (1, 0)
    multiple = num1 // num2
    remainder = (num1 % num2)
    (s, t) = extended_euclid(num2, remainder)
    return (t, s - multiple * t)


if __name__ == "__main__":
    num1 = int(input("First number? "))
    num2 = int(input("Second number? "))
    gcd = euclid_theory(num1, num2)
    print(f"GCD of ({num1}, {num2}): {gcd}")
    if gcd != 1:
        print("Modular inversion cannot be used to solve for Bezout's")
        exit()
    bezout = extended_euclid(num1, num2)
    print(f"Bezout's answer of ({num1}, {num2}): {bezout}")
