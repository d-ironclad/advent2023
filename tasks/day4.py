import pprint
import re
from .utils import get_file

NUMBERS_PATTERN = '\d+'

def get_score(card: dict):
    intersection = list(set(card["have"]) & set(card["win"]))
    score = 0
    wins = len(intersection)
    if len(intersection) > 0:
        score =  [1 * 2**i for i in range(len(intersection))][-1]
    return score, wins

def cards():
    lines = get_file("data_day4.txt")
    cards = []
    wins = []
    score = 0
    for line in lines:
        numbers = line.split(":")[1].split("|")
        score, win = get_score({"win": re.findall(NUMBERS_PATTERN, numbers[0]), "have": re.findall(NUMBERS_PATTERN, numbers[1])})
        cards.append(score)
        wins.append(win)

    pprint.pprint(cards, depth=3)
    score = sum(cards)
    # winning cards itself
    counter = [1] * len(wins)
    print(wins)
    # go through cards
    for idx, card in enumerate(wins):
        print(f"Index {idx} and wins", card)
        # win of each copy
        for i in range(idx+1, idx+card+1):
            print(f"Won {wins[i]} from card", i)            
            # accumulate!
            counter[i] += counter[idx]
            print("Upd cards ", counter[i])
    return score, sum(counter)