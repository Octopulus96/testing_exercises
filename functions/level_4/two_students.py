from typing import NamedTuple


class Student(NamedTuple):
    first_name: str
    last_name: str
    telegram_account: str | None


def get_student_by_tg_nickname(
    telegram_username: str,
    students: list[Student],
) -> Student | None:
    matched_students = [
        s
        for s in students
        if s.telegram_account and s.telegram_account.strip("@") == telegram_username
    ]
    return matched_students[0] if matched_students else None
