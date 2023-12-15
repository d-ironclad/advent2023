import re

NUMBERS_PATTERN = '\d+'

def get_file(path: str):
    with open(path, "r") as file:
        return file.readlines()

def get_int(string: str):
    return int(re.search(r'\d+', string).group())