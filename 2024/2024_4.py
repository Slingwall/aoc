from typing import List, Tuple, Any
import re

def search_diags(grid):
    diag_matches = 0
    for row in range(len(grid) - 3):
        for col in range(len(grid[0]) - 3):
            diag1 = "".join([grid[row][col], grid[row+1][col+1], grid[row+2][col+2], grid[row+3][col+3]])
            diag2 = "".join([grid[row+3][col], grid[row+2][col+1], grid[row+1][col+2], grid[row][col+3]])
            diag_matches += diag1 in "XMAS"
            diag_matches += diag1 in "SAMX"
            diag_matches += diag2 in "XMAS"
            diag_matches += diag2  in "SAMX"

    return diag_matches

def mas_search(grid):
    mas_matches = 0
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            mas1 = "".join([grid[row][col], grid[row + 1][col + 1], grid[row + 2][col + 2]])
            mas2 = "".join([grid[row][col + 2], grid[row + 1][col + 1], grid[row + 2][col]])
            mas_matches += (mas1 in "MAS" or mas1 in "SAM") and (mas2 in "MAS" or mas2 in "SAM")
            
    print(mas_matches)
    return mas_matches

def part1(data: List[str]) -> Any:
    """ 2024 Day 2 Part 1
    """

    # find how many times XMAS is spelled in rows
    row_matches = 0
    for line in data:
        found = re.findall(r"XMAS", line)
        found_back = re.findall(r"SAMX", line)
        row_matches += len(found)
        row_matches += len(found_back)

    print(row_matches)

    # convert to grid
    rows, cols = len(data[0]), len(data)
    grid = [[0 for x in range(rows)] for y in range(cols)] # explain this line

    for i in range(rows):
        for j in range(cols):
            grid[i][j] = data[i][j]

    # convert back to list of strings, but with cols and rows flipped
    total_strings = []
    for i in range(rows):
        cur_new_row = ""
        for j in range(cols):
            cur_new_row += grid[j][i]
        total_strings.append(cur_new_row)
    
    # find how many times XMAS is spelled in cols
    col_matches = 0
    for line in total_strings:
        found = re.findall(r"XMAS", line)
        found_back = re.findall(r"SAMX", line)
        col_matches += len(found)
        col_matches += len(found_back)

    # print(f"oh no = {col_matches}")

    matches = row_matches + col_matches + search_diags(grid)
    # print(matches)
    
    return NotImplemented


def part2(data: List[str]) -> Any:
    """ 2024 Day 2 Part 2
    """
    rows, cols = len(data[0]), len(data)
    grid = [[0 for x in range(rows)] for y in range(cols)] # explain this line

    for i in range(rows):
        for j in range(cols):
            grid[i][j] = data[i][j]

    mas_search(grid)

    # similar to search_diag but you just search diagonaly for either MAS or SAM
    # but if has to be a pair of either of the 2 combinations at the same time
    # and if that's true, then add one
   

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