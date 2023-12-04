import re

from .utils import get_file

SYMBOLS_PATTERN ='[^.|\d]'
NUMBERS_PATTERN = '[^.|\d]'

def is_adjacent_to_symbol(row: int, number: dict, pattern: str):
    # check for the end or beginning of the row
    start = 1 if number[0] == 0 else number[0]-1
    end = number[1]-1 if number[1] == len(row)-1 else number[1]+1
    if re.search(pattern, row[start:end]):   
        return True

def engine():
    lines = get_file("data_day3.txt")
    numbers_list = []

    for idx, line in enumerate(lines):
        numbers_list.append([])
        matches = re.finditer(r'(\d+)|(\*)', line)
        # collect all pairs of numbers coordinates and gears
        for match in matches:
            if match:
                numbers_list[idx].append((match.start(), match.end(), match.group()))
    sum = 0
    gears = 0
    for idx, row in enumerate(numbers_list):
        # determine up and down rows)
        print('Row', idx)
        # For power
        up_down_rows = lines[idx-1] if idx > 0 else None, lines[idx+1] if idx+1 < len(numbers_list) else None
        # For gears
        up_down_numbers =  numbers_list[idx-1] if idx > 0 else None, numbers_list[idx+1] if idx+1 < len(numbers_list) else None
        # print('Up-down symbol rows', up_down_rows)
        for item in row:
            print("number", lines[idx][item[0]:item[1]])
            if item[2] != '*':
                adjacent = []
                # check up and down
                for neighbor_row in up_down_rows:
                    if neighbor_row:
                        adjacent.append(is_adjacent_to_symbol(neighbor_row.rstrip(), item, pattern=SYMBOLS_PATTERN))
                #check left and right
                adjacent.append(is_adjacent_to_symbol(lines[idx].rstrip(), item, pattern=SYMBOLS_PATTERN))
                if any(adjacent):
                    sum += int(item[2])
            else:
                print('Checking gear', item)
                adjacent = []
                # check up nad down
                for neighbor_row in up_down_numbers:
                    print('neighbor row', neighbor_row)
                    if neighbor_row:
                        for number in neighbor_row:
                            if number[2] != '*' and (
                                number[0] <= item[0] <= number[1]-1 or item[1] == number[0] or item[0] == number[1]):
                                adjacent.append(number[2])
                # check right left
                adjacent += [number[2] for number in numbers_list[idx] if number[0] == item[1] or number[1] == item[0]]
                if len(adjacent) == 2:
                    gears += (int(adjacent[0]) * int(adjacent[1]))
                print(adjacent)

    return sum, gears