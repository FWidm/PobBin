import os

ROOT = os.path.abspath(os.path.dirname(__file__))

def read_asset(file_name: str):
    with open(f"{ROOT}{os.sep}{file_name}", 'r') as f:
        return f.readlines()
