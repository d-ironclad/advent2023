import re
from itertools import accumulate
from .utils import get_file

NUMBERS_PATTERN = '\d+'
def cards():
    lines = get_file("data_day4.txt")
    cards = []
    score = 0
    for line in lines:
        numbers = line.split(":")[1].split("|")
        cards.append(
            {"num": line.split(":")[0], "win": re.findall(NUMBERS_PATTERN, numbers[0]), "have": re.findall(NUMBERS_PATTERN, numbers[1])}
        )

    print(cards)
    for card in cards:
        intersection = list(set(card["have"]) & set(card["win"]))
        if len(intersection) > 0:
            progression = [1 * 2**i for i in range(len(intersection))]
            score += progression[-1]

    return score