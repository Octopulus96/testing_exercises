def delete_remove_brackets_quotes(name: str) -> str:
    if name[0] == "{":
        return name[2 : len(name) - 2]
    return name
