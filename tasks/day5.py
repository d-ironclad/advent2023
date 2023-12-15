import re
from .utils import get_file, NUMBERS_PATTERN

def get_data():
    lines = get_file("data_day5")
    seeds = [int(x) for x in re.findall(NUMBERS_PATTERN, lines[0])]
    maps = {}
    
    current_map = None
    for line in lines[2:]:
        print(current_map)
        if line.endswith(":\n"):
            current_map = line.split(' ')[0]
            maps[current_map] = []
        if re.match(NUMBERS_PATTERN, line):
            print(current_map)
            maps[current_map].append([int(x) for x in re.findall(NUMBERS_PATTERN, line)])
    
    return seeds, maps

def seeds():
    for seed in seeds:
        pass
        for map in maps:
            source_start = map[0]
            destination_start = map[1]
            length = map[2]
    
    seeds, maps = get_data()

    return seeds, maps
