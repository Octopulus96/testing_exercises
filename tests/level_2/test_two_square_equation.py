import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        pytest.param(
            1,
            -3,
            2,
            (1.0, 2.0),
            id="discriminant_is_zero_and_the_equation_has_one_solution",
        ),
        pytest.param(
            0,
            1,
            0,
            (0.0, None),
            id="discriminant_is_negative_and_the_equation_has_no_solutions",
        ),
        pytest.param(
            1,
            -3,
            3,
            (None, None),
            id="discriminant_is_negative_and_the_equation_has_no_solutions",
        ),
        pytest.param(
            0,
            2,
            3,
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
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )


@pytest.fixture()
def fake_3_items_tuple() -> tuple[int | str, ...]:
    letters: list[str] = [chr(i) for i in range(ord("a"), ord("a") + 26)]
    numbers: list[int] = list(range(-9, 10))
    combined_list: list[str | int] = letters + numbers
    combined_tuple: tuple[int | str, ...] = tuple(combined_list)
    return combined_tuple[:3]


def test__solve_square_equation__str_arguments_causes_TypeError(
    fake_3_items_tuple,
) -> None:
    square_coefficient, linear_coefficient, const_coefficient = fake_3_items_tuple
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
