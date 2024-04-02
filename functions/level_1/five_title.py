import re


def change_copy_item(title: str, max_main_item_title_length: int = 100) -> str:

    additional_copy_text: str = "Copy of"
    title_with_additional_copy_text: str = f"{additional_copy_text} {title}"

    if len(title_with_additional_copy_text) >= max_main_item_title_length:
        return title
    if not title.startswith(additional_copy_text):
        return title_with_additional_copy_text

    last_element = title.split()[-1]
    element_in_brackets = last_element.split("(")[-1].split(")")[0]
    has_copy_number = all(
        [re.search(r"\(\d+\)", last_element), element_in_brackets.isdigit()]
    )
    return (
        title.replace(title.split()[-1], f"({int(element_in_brackets) + 1})")
        if has_copy_number
        else f"{title} (2)"
    )
