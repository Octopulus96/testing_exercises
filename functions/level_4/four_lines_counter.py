import os


def count_lines_in(filepath: str) -> int | None:
    if not os.path.isfile(filepath):
        return None
    with open(filepath, "r") as file_handler:
        lines = file_handler.readlines()
    return sum(1 for l in lines if not l.lstrip().startswith("#"))
