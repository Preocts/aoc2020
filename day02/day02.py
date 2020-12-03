"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 1 part 1
"""
import re


def get_min(line: str) -> int:
    return int(line.split("-")[0])


def get_max(line: str) -> int:
    return int(line.split("-")[1].split(" ")[0])


def get_char(line: str) -> int:
    return line.split(":")[0].split(" ")[1]


def validate_rule(
    minimum: int, maximum: int, character: str, password: str
) -> bool:
    occurance = len(re.findall(f"{character}", password))
    result = "Valid Password"
    print_line = "{:^3d} {:^3d} {:^3d} | {:^3s} | {:<25s} | {:s}".format

    if minimum > occurance:
        result = f"Minimum violated ({minimum - occurance})"

    if maximum < occurance:
        result = f"Maximum violated ({occurance - maximum})"

    if not occurance:
        result = "Requied violated (missing)"

    print(print_line(minimum, occurance, maximum, character, password, result))

    return True if result == "Valid Password" else False


def main01(fileinput: tuple, prefix: str = "") -> None:
    print("Results for that sled rental place down the street:")
    count = 0
    for input_ in fileinput:
        if validate_rule(
            get_min(input_),
            get_max(input_),
            get_char(input_),
            input_.split(" ").pop(),
        ):
            count += 1

    print(f"\n{prefix}Total Valid: {count}")
    print(f"Total iterations: {len(fileinput)}")
    return None


def validate_toboggan(
    first: int, second: int, character: str, password: str
) -> bool:
    check = f"{password[first - 1]}{password[second - 1]}"
    result = "Valid Password"
    print_line = "{:^3d} {:^3d} {:^4s} | {:^3s} | {:<25s} | {:s}".format

    if not len(re.findall(character, check)):
        result = "Invalid: Missing required letter"
    if len(re.findall(character, check)) > 1:
        result = "Invalid: Too many occurrences"

    print(print_line(first, second, check, character, password, result))

    return True if result == "Valid Password" else False


def main02(fileinput: tuple, prefix: str = "") -> None:
    print("Results for Toboggan Corporate Authentications System:")
    count = 0
    for input_ in fileinput:
        if validate_toboggan(
            get_min(input_),
            get_max(input_),
            get_char(input_),
            input_.split(" ").pop(),
        ):
            count += 1

    print(f"\n{prefix}Total Valid: {count}")
    print(f"Total iterations: {len(fileinput)}")
    return None


if __name__ == "__main__":
    test_sample = (
        "1-3 a: abcde",
        "1-3 e: cdefg",
        "2-9 c: ccccccccc",
        "1-3 a: aaa",
        "1-3 a: bbb",
        "1-3 a: aaaa",
        "7-8 x: qxrxmxccxxx",
    )

    with open("inputfile", "r") as f:
        file_sample = f.read().split("\n")

    # main01(test_sample, "[TEST] ")
    main01(file_sample)

    print("\n" + "#" * 72 + "\n")

    # main02(test_sample, "[TEST] ")
    main02(file_sample)
