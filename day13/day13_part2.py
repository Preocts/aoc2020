"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day13
"""
import sys

import euclidtheory
import modularinverse


def check_all_values(timemark: int, bus_list: list, pointer: int = 1) -> bool:
    if pointer == len(bus_list):
        return True
    if bus_list[pointer] == 0:
        return check_all_values(timemark, bus_list, pointer + 1)
    if (timemark + pointer) % bus_list[pointer]:
        return False
    return check_all_values(timemark, bus_list, pointer + 1)


def chinese_remainder_theorem(n1: int, r1: int, n2: int, r2: int) -> int:
    """
    >>> chinese_remainder_theorem(5,1,7,3)
    31
    Explanation : 31 is the smallest number such that
                (i)  When we divide it by 5, we get remainder 1
                (ii) When we divide it by 7, we get remainder 3
    >>> chinese_remainder_theorem(6,1,4,3)
    14
    """
    (x, y) = euclidtheory.extended_euclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m


def main(input_file) -> None:
    input_line = input_file[1].replace('x', '0')
    bus_id_list = [int(i) for i in input_line.split(",")]
    offset_list = []
    full_multiple = 1
    for idx, bus in enumerate(bus_id_list):
        if not bus:
            continue
        offset_list.append((bus, idx + 1,))
        full_multiple *= bus
    print(bus_id_list)
    print(offset_list)
    print(full_multiple)

    test_id = offset_list[0][0]
    test_remainder = offset_list[0][1]

    multiple = full_multiple // test_id
    print(test_id, test_remainder, multiple)
    print(multiple % test_id)
    inverse = modularinverse.modular_inverse(multiple, test_id)
    print(inverse, (multiple * inverse) % test_id)


    return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Useage: python day13.py [filename]")
        exit()

    try:
        with open(sys.argv[1], "r") as f:
            input_file = f.read().split("\n")
    except Exception as err:
        print("I can't do that, Dave.")
        print(f">>> {err}")
        exit()
    main(tuple(input_file))

    exit()
