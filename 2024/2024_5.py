from typing import List, Tuple, Any
import re
from collections import defaultdict


def part1(data: List[str]) -> Any:
    """ 2024 Day 2 Part 1
    """

    # have brandon explain time complexity of mine and his
    sum = 0
    page_rules = defaultdict(list)
    updates = []
    updates_list = []
    correct_updates = []
    ordering = True
    # print(data)

    for index, line in enumerate(data):
        if len(line) == 0:
            updates = data[index + 1:]
            break
        page_rules[line[0:2]].append(line[3:5])
        
    print(updates)    
    # split elements in updates into individual strings
    for e in updates:
        x = re.split(r",", e)
        updates_list.append(x)

    # print(updates_list)
    for e in page_rules.items():
        print(e)

    cur_page = ""

    for update in updates_list:
        cur_page = update[0]
        print(f"cur page = {cur_page}")
        for page in update:
            # print(page)
            if page == cur_page:
                continue
            print(cur_page)
            print(f"rules for the 2nd pointer: {page_rules.get(page)}")
            if cur_page in page_rules.get(page):
                ordering = False
        if ordering == False:
            break
        else:
            correct_updates.append(update)
    
    print(f"correct updates = {correct_updates}")



    # check if for each key if the values in front of it 


    return NotImplemented


def part2(data: List[str]) -> Any:
    """ 2024 Day 2 Part 2
    """
    
  
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