""" Find the modular inverse

Author: Preocts <preocts@preocts.com>
"""

import euclidtheory


def modular_inverse(num1: int, num2: int) -> int:
    """ Returns the modular inverse, returns 0 if no inverse

    Where num1(x) = 1(mod num1), find x
    """
    gcd = euclidtheory.euclid_theory(num1, num2)

    if gcd != 1:
        return 0

    (_, t) = euclidtheory.extended_euclid(num1, num2)
    return abs(t)


print(modular_inverse(7, 3))
