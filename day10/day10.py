"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day10
"""
from collections import defaultdict
import sys


def this_cant_be_safe(adaptors: tuple) -> dict:
    """ It really can't """
    joltage = 0
    diffs = {"0": 0, "1": 0, "2": 0, "3": 1}
    for jump in sorted(adaptors):
        diff = jump - joltage
        if diff > 3:
            print(f"{jump} too damn high.")
            exit()
        diffs[str(diff)] += 1
        joltage = jump
    return diffs


def locked_count(adaptors: tuple) -> list:
    """ The number of values that cannot be moved """
    unsorted_mess = list(adaptors)
    unsorted_mess.append(0)
    sorted_mess = sorted(unsorted_mess)
    sorted_mess.append(sorted_mess[-1] + 3)
    locked = [0]
    joltage = 0
    for index in range(1, len(sorted_mess) - 1):
        # 3 diff are locked
        # print(sorted_mess[index + 1] - sorted_mess[index])
        if sorted_mess[index + 1] - sorted_mess[index] == 3:
            locked.append(0)
            joltage = sorted_mess[index]
            continue
        # print(sorted_mess[index] - sorted_mess[index - 1])
        if sorted_mess[index] - sorted_mess[index - 1] == 3:
            locked.append(0)
            joltage = sorted_mess[index]
            continue
        locked.append(sorted_mess[index] - joltage)
        joltage = sorted_mess[index]
    locked.append(0)
    # print(sorted_mess)
    # print(f"Lock length = {len(locked)}")
    # print(locked)
    # print(f"sum : {sum(locked)}")
    # print(sum(locked) ** 2 )

    size = 0
    total = 1
    for lock in locked[1:len(locked) - 1]:
        if lock:
            size = size + 1
        if not lock:
            if size == 1:
                total = total * 2
            if size == 2:
                total = total * 4
            if size == 3:
                total = total * 7
            size = 0
    # print("WTF")
    # paths = defaultdict(int)
    # paths[0] = 1
    # for item in sorted_mess[1:len(sorted_mess)-1]:
    #     paths[item] = paths[item - 1] + paths[item - 2] + paths[item - 3]
    #     print(
    #         f"{item}, {paths[item]} = {paths[item - 1]} + {paths[item - 2]} + {paths[item - 3]}")
    # print(paths[sorted_mess[-2]])
    # exit()
    return total


def main(input_file: tuple) -> None:
    diffs = this_cant_be_safe(input_file)

    # print(diffs)
    print(f"Answer one: {diffs['1'] * diffs['3']}")

    combos = locked_count(input_file)

    print(f"Answer two: {combos}")

    return


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Useage: python day10.py [filename]")
        exit()

    try:
        with open(sys.argv[1], "r") as f:
            input_file = f.read().split("\n")
    except Exception as err:
        print("I can't do that, Dave.")
        print(f">>> {err}")
        exit()
    int_tuple = tuple(map(int, input_file))
    main(int_tuple)

    exit()
