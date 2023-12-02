import re
from functools import reduce
num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_code(line: str):
    
    matches = re.findall(r'(?=(\d))|(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))', line)

     # Printing number
    print(f'Line: {line}')
    sum = ''
    for i in [matches[0], matches[-1]]:
        num = reduce(lambda x, y: x or y, i)
        if len(num) > 1:
            i = str(num_map[num])
        else:
            i = num
        print(f'Calibration: {i}')
        sum += i

    print(f'Final sum: {sum}\n')
    return int(sum)
    
    
def calibration():
    lines = []
    with open("data_day1.txt", "r") as file:
        lines = file.readlines()

    code = 0
    for line in lines:
        code = code + get_code(line)  
    return code