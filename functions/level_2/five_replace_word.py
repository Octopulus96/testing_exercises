def replace_word(text: str, replace_from: str, replace_to: str) -> str:
    words = text.split()

    new_words = []
    for word in words:
        if word.lower() == replace_from.lower():
            new_words.append(replace_to)
        else:
            new_words.append(word)

    return " ".join(new_words)
