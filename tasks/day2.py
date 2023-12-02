import re
import operator
from collections import Counter
from functools import reduce
from .utils import get_file, get_int

def load_data():
    lines = get_file("data_day2.txt")

    result = {}
    for line in lines:
        game = line.split(":")
        result[get_int(game[0])] = [
            {
                r.strip().split(" ")[1]: int(r.strip().split(" ")[0]) for r in round.split(",")
            } for round in game[1].split(";")
        ]

    return result
def cubes_game(do_break=False):
    games = load_data()
    condition = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    power = 0
    for game in games:
        print(f"Game {game}")
        flag = False
        minimal = {}
        game_power = 0
        for round in games[game]:
            
            print("Round: ", round)
            if not minimal:
                minimal = round
            for k, v in round.items():
                if minimal.get(k, 0) < v:
                    minimal[k] = v
            result = Counter(condition)
            result.subtract(Counter(round))
            print("Comparison: ", dict(result))

            if not all([x >= 0 for x in dict(result).values()]):
                print(f"Game {game} is impossible!\n")
                flag = True
                if do_break:
                    break
        power += reduce(operator.mul, list(minimal.values()), 1)     
        if not flag:
            print(f"Game {game} is possible\n")
            sum += game
    return sum, power