import math


def solve_square_equation(
    square_coefficient: float,
    linear_coefficient: float,
    const_coefficient: float,
) -> tuple[float | None, float | None]:
    discriminant = linear_coefficient**2 - 4 * square_coefficient * const_coefficient

    if discriminant < 0:
        return None, None

    if not square_coefficient:
        if linear_coefficient:
            return -const_coefficient / linear_coefficient, None
        else:
            return None, None

    root_left = (-linear_coefficient - math.sqrt(discriminant)) / (
        2 * square_coefficient
    )
    root_right = (-linear_coefficient + math.sqrt(discriminant)) / (
        2 * square_coefficient
    )
    return root_left, root_right
