from typing import List, Tuple, Any


grid = []
guard_row = 0
guard_col = 0
guard_ds = ['V', '^', '>', '<']
cur_d = ''
    
# hopefully move the guard
def move(grid, guard_row, guard_col, direction):
    distinct_pos = 0
    while (guard_row < len(grid) - 1 and guard_row > 0) and (guard_col < len(grid[0]) - 1 and guard_col > 0):
        # print(f"guard row & col: {guard_row, guard_col}")
        # print(distinct_pos)
        if direction == 'V':
            grid[guard_row][guard_col] = 'X'
            if grid[guard_row + 1][guard_col] == '#':
                direction = '<'
            elif grid[guard_row + 1][guard_col] == '.':
                distinct_pos += 1
                guard_row += 1
            else:
                guard_row += 1
        elif direction == '^':
            grid[guard_row][guard_col] = 'X'
            if grid[guard_row - 1][guard_col] == '#':
                direction = '>'
            elif grid[guard_row - 1][guard_col] == '.':
                distinct_pos += 1
                guard_row -= 1
            else:
                guard_row -= 1
        elif direction == '>':
            grid[guard_row][guard_col] = 'X'
            if grid[guard_row][guard_col + 1] == '#':
                direction = 'V'
            elif grid[guard_row][guard_col + 1] == '.':
                distinct_pos += 1
                guard_col += 1
            else:
                guard_col += 1
        elif direction == '<':
            grid[guard_row][guard_col] = 'X'
            if grid[guard_row][guard_col - 1] == '#':
                direction = '^'
            elif grid[guard_row][guard_col - 1] == '.':
                distinct_pos += 1
                guard_col -= 1
            else:
                guard_col -= 1

    return distinct_pos + 1

def part1(data: List[str]) -> Any:
    """ 2024 Day 2 Part 1
    """

    # turn our input into a grid
    for line in data:
        list_row = []
        for char in line:
            list_row.append(char)
        grid.append(list_row)
    
    # find guard
    for index, line in enumerate(grid):
        for i2, char in enumerate(line):
            if char in guard_ds:
                guard_row = index
                guard_col = i2

    # initial guard direction
    cur_d = grid[guard_row][guard_col]

    total = move(grid, guard_row, guard_col, cur_d)

    # for line in grid:
    #     print(line)
    # print(f"guard row = {guard_row}")
    # print(f"guard col = {guard_col}")
    print(f"TOTAL!!!! = {total}")

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