import collections
import operator

from functions.level_3.models import Expense


def is_subscription(expense: Expense, history: list[Expense]) -> bool:
    same_destination_expenses = sorted(
        [e for e in history if e.spent_in == expense.spent_in],
        key=operator.attrgetter("spent_at"),
    )

    month_to_expenses_amount = collections.defaultdict(int)
    for expense in same_destination_expenses:
        month_to_expenses_amount[expense.spent_at.month] += 1

    return (
        len(same_destination_expenses) >= 3
        and max(month_to_expenses_amount.values()) == 1
    )
