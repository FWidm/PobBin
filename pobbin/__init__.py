import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))+os.sep+".."+os.sep


def load_file_as_string(path: str) -> str:
    with open(ROOT_DIR + os.sep + os.sep + path, "r") as file:
        return file.read()
