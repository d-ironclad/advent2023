import re

from .utils import get_file

def is_adjacent_to_symbol(row: int, number: dict):
    # check for the end or beginning of the row
    start = 1 if number[0] == 0 else number[0]-1
    end = number[1]-1 if number[1] == len(row)-1 else number[1]+1
    print('search substring', row[start:end])
    if re.search('[^.|\d]', row[start:end]):   
        return True


def engine():
    lines = get_file("data_day3.txt")
    numbers_list = []

    for idx, line in enumerate(lines):
        print(line)
        numbers_list.append([])
        matches = re.finditer(r'\d+', line)
        # collect all pairs of numbers coordinates
        for match in matches:
            numbers_list[idx].append((match.start(), match.end()))
    print(numbers_list)
    sum = 0
    for idx, row in enumerate(numbers_list):
        # determine up and down rows)
        print('Row', idx)
        up_down_rows = (lines[idx-1] if idx > 0 else None, lines[idx+1] if idx+1 < len(numbers_list) else None)
        print('Up-down rows', up_down_rows)
        for number in row:
            print("number", lines[idx][number[0]:number[1]])
            if number:
                adjacent = []
                # check up and down
                for neighbor_row in up_down_rows:
                    if neighbor_row:
                        adjacent.append(is_adjacent_to_symbol(neighbor_row.rstrip(), number))
                #check left and right
                adjacent.append(is_adjacent_to_symbol(lines[idx].rstrip(), number))
                if any(adjacent):
                    print("adding",lines[idx][number[0]:number[1]], )
                    sum += int(lines[idx][number[0]:number[1]])
    return sum