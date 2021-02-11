from pathlib import Path

from pobbin import ROOT_DIR


def load_test_file_bytes(path: str) -> bytes:
    with open(Path(ROOT_DIR, 'tests', path), "rb") as file:
        return file.read()


def load_test_file(path: str) -> str:
    with open(Path(ROOT_DIR, 'tests', path), "r") as file:
        return file.read()
