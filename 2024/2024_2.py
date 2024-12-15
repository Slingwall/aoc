from typing import List, Tuple, Any

unsafe_levels = []

def part1(data: List[str]) -> Any:
    """ 2024 Day 2 Part 1
    """

    int_reports = []
    cur = 0
    cur2 = 0
    safe_reports = 0
    

    for x in data:
        safe = True
        each = x.split(" ")
        for y in each:
            int_reports.append(int(y))
        temp = int_reports[:]
        cur = int_reports[0]
        if all(a == b for a, b in zip(sorted(temp), int_reports)):
            # ascending
            for j in int_reports[1:]:
                if not (j - cur <= 3 and j - cur >= 1):
                    # unsafe levels
                    unsafe_levels.append(int_reports.copy())
                    safe = False
                if safe == False:
                    break
                cur = j
        elif all(a == b for a, b in zip(sorted(temp, reverse=True), int_reports)):
            # descending
            for j in int_reports[1:]:
                if not (cur - j <= 3 and cur - j >= 1):
                    unsafe_levels.append(int_reports.copy())
                    safe = False
                if safe == False:
                    break
                cur = j
        else:
            unsafe_levels.append(int_reports.copy())
            safe = False
        
        if safe == True:
            safe_reports += 1

        int_reports.clear()

    print(f"{safe_reports=}")

    return safe_reports


def part2(data: List[str]) -> Any:
    """ 2024 Day 2 Part 2
    """
    new_safe = 0
    count = 0

    for e in unsafe_levels:
        for ie in range(0, len(e)):
            one_safe = True
            temp = e.copy()
            temp2 = e.copy()
            temp.pop(ie)
            temp2.pop(ie)
            cur = temp[0]
            if all(a == b for a, b in zip(sorted(temp), temp2)):
                for j in temp[1:]:
                    if not (j - cur <= 3 and j - cur >= 1):
                        one_safe = False
                    cur = j
            elif all(a == b for a, b in zip(sorted(temp, reverse=True), temp2)):
                for j in temp[1:]:
                    if not (cur - j <= 3 and cur - j >= 1):
                        one_safe = False
                    cur = j
            else:
                one_safe = False

            if (one_safe):
                new_safe += 1
                break
    
    total = new_safe + part1(data)
    print("cur num of new safe guys= " + str(total))


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