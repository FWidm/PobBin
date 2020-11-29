from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


def load_file_as_string(path: str) -> str:
    with open(Path(ROOT_DIR, path), "r") as file:
        return file.read()
