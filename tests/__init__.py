from pathlib import Path

from pobbin import ROOT_DIR


def load_file_as_bytes(path: str) -> bytes:
    with open(Path(ROOT_DIR, path), "rb") as file:
        return file.read()
