"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day07
"""
import sys

all_the_bags = dict()


def parse_it(fileinput: list) -> dict:
    bags_in_bags = {}
    for line in fileinput:
        clean = line.replace("bags", "").replace("bag", "").replace(".", "")
        start_and_nested = clean.split(" contain ")
        nested_group = {}
        for bags in start_and_nested[1].split(", "):
            clipped = bags.split(" ", 1)
            if clipped[0] in "no":
                continue
            nested_group[clipped[1].strip()] = int(clipped[0])
        bags_in_bags[start_and_nested[0].strip()] = nested_group
    return bags_in_bags


def deep_dive(staring_bag: str, deep: int = 0) -> bool:
    """ WTF """
    final_searches = []
    found_gold = False
    for bag in all_the_bags.get(staring_bag, {}):
        if bag == "shiny gold":
            return True
        found_gold = deep_dive(bag, deep + 1)
        final_searches.append(found_gold)
    return any(final_searches)


def chain_dive(staring_bag: str, chain: str = "") -> str:
    if not all_the_bags.get(staring_bag, {}):
        return chain
    final_chain = ""
    for bag in all_the_bags.get(staring_bag, {}):
        if not chain:
            full_chain = chain_dive(bag, f"{staring_bag},{bag}")
        else:
            full_chain = chain_dive(bag, f"{chain},{bag}")
        final_chain += full_chain
    return final_chain


def counting_bags(staring_bag: str, count: int = 0) -> int:
    """ WTF 2 the re-WTF'ening """
    if not all_the_bags.get(staring_bag, {}):
        return 0
    final_counts = []

    for bag, inside_count in all_the_bags.get(staring_bag, {}).items():
        stepped_count = counting_bags(bag, inside_count)
        multiple_count = (inside_count + inside_count * stepped_count)

        final_counts.append(multiple_count)
    return sum(final_counts)


def main(input_file):
    global all_the_bags
    all_the_bags = parse_it(input_file)

    dict_compare = []
    for idx, dicts in enumerate(all_the_bags):
        if dicts in dict_compare:
            print(f"Duplicate dict: {dict}, {idx + 1}")
        dict_compare.append(dicts)
    print(f"Length the input: {len(all_the_bags)}")

    count = 0
    for bag in all_the_bags:
        if deep_dive(bag):
            count += 1

    print(f"Part one anwser: {count}")

    print(f"Part two answer: {counting_bags('shiny gold')}")


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

    main(input_file)

    exit()
