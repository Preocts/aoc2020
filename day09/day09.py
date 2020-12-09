"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day09
"""
import sys


def rainbow_gen(pream_group: tuple) -> tuple:
    rainbow_table = []
    for index01 in range(len(pream_group)):
        for index02 in range(len(pream_group)):
            rainbow_table.append(pream_group[index01] + pream_group[index02])
    # print(pream_group)
    # print(rainbow_table)
    return tuple(rainbow_table)


def deep_scan(full_list: tuple, target: int) -> list:

    for index01 in range(len(full_list)):
        contiguous_list = []
        for value in full_list[index01:]:
            contiguous_list.append(value)
            if sum(contiguous_list) > target:
                break
            if sum(contiguous_list) == target:
                return contiguous_list
    return []


def main(input_file: tuple, pream: int) -> None:

    for index in range(len(input_file)):
        pointer = input_file[index + pream]
        # print(pointer)
        if pointer not in rainbow_gen(input_file[index:index + pream]):
            print(f"Weak-point found: {pointer}")
            break

    break_code = sorted(deep_scan(input_file, pointer))
    # not 1631469, forgot to sort like a smartie I am.
    print(f"Break-point: {break_code[0] + break_code[-1]}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Useage: python day09.py [filename] [preamble_size]")
        exit()

    try:
        with open(sys.argv[1], "r") as f:
            input_file = f.read().split("\n")
    except Exception as err:
        print("I can't do that, Dave.")
        print(f">>> {err}")
        exit()
    int_tuple = tuple(map(int, input_file))
    main(int_tuple, int(sys.argv[2]))

    exit()
