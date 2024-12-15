from typing import List, Tuple, Any
import re

def get_full_string_total(full_string):
    matches = re.findall(r"mul\(\d+,\d+\)", full_string)

    total = 0
    for e in matches:
        split_by_nums = re.split(",", e)
        e1 = re.findall(r"\d+", split_by_nums[0])
        e2 = re.findall(r"\d+", split_by_nums[1])
        # print(e1)
        product = int(e1[0]) * int(e2[0])
        total += product

    return total


def part1(data: List[str]) -> Any:
    """ 2024 Day 2 Part 1
    """

    all_lines = ""
    for line in data:
        all_lines += line.strip()

    total = get_full_string_total(all_lines)

    # uncomment this for part 1 answer ---------------------------------------
    print(f"part 1 total = {total}")

    return NotImplemented


def part2(data: List[str]) -> Any:
    """ 2024 Day 2 Part 2
    """
    
    all_lines = ""
    for line in data:
        all_lines += line.strip()

    # print(all_lines)
    do_and_dont = re.split(r"(don't\(\)).*?(do\(\))|don't\(\).+?\Z", all_lines)
    # print(do_and_dont)

    grand_total = 0
    for i in range(0, len(do_and_dont)):
        if (do_and_dont[i] is not None):
            # print(do_and_dont[i])
            # print(f"each do = {do_and_dont[e]}")
            grand_total += get_full_string_total(do_and_dont[i])
            # print(f"each total = {grand_total} ")

    print(f"grand total = {grand_total}")


    return NotImplemented


def main(verbose: bool=False) -> Tuple[Tuple[Any, float]]:
    from pathlib import Path
    import sys, re
    sys.path.append(str(Path(__file__).parent.parent))
    # from Modules.timer import Timer
    year, day = re.findall(r'\d+', str(__file__))[-2:]
    
    with open(Path(__file__).parent.parent / f"Inputs/{year}_{day}.txt", encoding='UTF-8') as f:
        data = [line.strip('\n') for line in f.readlines()]

    p1 = part1(data)
    p2 = part2(data)

    return (p1, ), (p2, )

    # with Timer() as p1_time:
    #     p1 = part1(data)

    # if verbose:
    #     print(f"\nPart 1:\n {p1}\nRan in {p1_time.elapsed:0.4f} seconds")

    # with Timer() as p2_time:
    #     p2 = part2(data)

    # if verbose:
    #     print(f"\nPart 2:\n {p2}\nRan in {p2_time.elapsed:0.4f} seconds")

    # return (p1, p1_time.elapsed), (p2, p2_time.elapsed)


if __name__ == "__main__":
    main(True)