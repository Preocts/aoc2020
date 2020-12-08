"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day08
"""
import sys


def find_bug(input_file: tuple, changed: list = []) -> int:
    if not changed:
        changed = [0 for _ in range(0, len(input_file))]
    # print(sum(changed))

    ran_once = [0 for _ in range(0, len(input_file))]
    acc_value = 0
    index = 0
    hacked = False
    while True:
        if index > len(input_file) - 1:
            return acc_value

        if ran_once[index]:
            acc_value = find_bug(input_file, changed)
            return acc_value
        ran_once[index] = 1
        command, value = input_file[index].split(" ")

        if not hacked:
            if command in "nop" and int(value) and not(changed[index]):
                # print("HACKED NOP")
                command = "jmp"
                changed[index] = 1
                hacked = True
            elif command in "jmp" and not(changed[index]):
                # print("HACKED JMP")
                command = "nop"
                changed[index] = 1
                hacked = True

        if command in "jmp":
            index += int(value)
            continue
        if command in "acc":
            acc_value += int(value)

        # print(f"Ran Once: {ran_once}")
        # print(f"Changed : {changed}")
        # input("")

        index += 1


def main(input_file: tuple) -> None:
    ran_once = [0 for _ in range(0, len(input_file))]
    acc_value = 0
    index = 0
    while True:
        if ran_once[index]:
            break
        ran_once[index] = 1
        command, value = input_file[index].split(" ")
        if command in "jmp":
            index += int(value)
            continue
        if command in "acc":
            acc_value += int(value)
        index += 1
    print(f"Answer for part one: {acc_value}")

    print(f"Answer for part two: {find_bug(input_file)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Useage: python day07.py [filename]")
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
