import string

from assets import read_asset
from pobbin.util.generate_url_key import build

monsters = read_asset('monsters.txt')
adjectives = read_asset('adjectives.txt')

def sort_by_keys(lst):
    lst.sort(key=len)
    return lst

x=sort_by_keys(monsters)[-1]
y=sort_by_keys(adjectives)[-2:]
name = f"{''.join([string.capwords(e.strip()) for e in y])}{x.strip()}"
print(name, len(name))

for i in range(100):
    print(build())