import string
import random


def build(length: int = 8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))
