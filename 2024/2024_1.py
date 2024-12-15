from typing import List, Tuple, Any


def part1(data: List[str]) -> Any:
    """ 2024 Day 1 Part 1
    """

    list1 = []
    list2 = []

    for x in data:
        each = x.split(" ")
        list1.append(int(each[0]))
        list2.append(int(each[-1]))

    list1.sort()
    list2.sort()

    count = 0
    distance = 0

    for j in list1:
         distance += abs((j - list2[count]))
         count += 1

    print(distance)

    # print(list1)

    return NotImplemented


def part2(data: List[str]) -> Any:
    """ 2024 Day 1 Part 2
    """

    list1 = []
    list2 = []

    for x in data:
        each = x.split(" ")
        list1.append(int(each[0]))
        list2.append(int(each[-1]))

    list1.sort()
    list2.sort()

    similarity = 0

    for j in list1:
        count = 0
        for k in list2:
            if j == k:
                count += 1
        similarity += (j * count)
    
    print(similarity)

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