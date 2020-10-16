import string

from assets import read_asset
import random

adjectives = read_asset("adjectives.txt")
monsters = read_asset("monsters.txt")


def build(adjective_count: int = 2):
    chosen_adjectives = []
    for i in range(adjective_count):
        adjective = random.choice(adjectives)
        while adjective in chosen_adjectives:
            adjective = random.choice(adjectives)
        chosen_adjectives.append(adjective)

    monster = string.capwords(random.choice(monsters))

    adjectives_string = "".join([string.capwords(word) for word in chosen_adjectives])

    return f"{adjectives_string}{monster}"
