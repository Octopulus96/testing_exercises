from typing import Union, List, Tuple, Any
import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        pytest.param(
            1.0,
            -3.0,
            2.0,
            (1.0, 2.0),
            id="discriminant_is_zero_and_the_equation_has_one_solution",
        ),
        pytest.param(
            0.0,
            1.0,
            0.0,
            (0.0, None),
            id="discriminant_is_negative_and_the_equation_has_no_solutions",
        ),
        pytest.param(
            1.0,
            -3.0,
            3.0,
            (None, None),
            id="discriminant_is_negative_and_the_equation_has_no_solutions",
        ),
        pytest.param(
            0.0,
            2.0,
            3.0,
            (-1.5, None),
            id="discriminant_is_positive_and_the_equation_has_two_solutions",
        ),
    ],
)
def test__solve_square_equation__obtaining_desrementant_and_solution_methods(
    square_coefficient: float,
    linear_coefficient: float,
    const_coefficient: float,
    expected: float,
) -> None:
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected


@pytest.fixture()
def fake_3_items_tuple() -> Tuple[Any, Any, Any]:
    letters: List[str] = [chr(i) for i in range(ord("a"), ord("a") + 26)]
    numbers: List[int] = list(range(-9, 10))
    combined_list: List[Any] = letters + numbers
    combined_tuple: Tuple[Any, ...] = tuple(combined_list)
    return (combined_tuple[0], combined_tuple[1], combined_tuple[2])


def test__solve_square_equation__str_arguments_causes_type_error(
    fake_3_items_tuple: Tuple[Any, Any, Any],
) -> None:
    square_coefficient, linear_coefficient, const_coefficient = fake_3_items_tuple
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
