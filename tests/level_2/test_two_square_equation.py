import pytest

from functions.level_2.two_square_equation import solve_square_equation

@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (1, -3, 2, (1.0, 2.0)),
        (0, 1, 0, (0.0, None)),
        (1, -3, 3, (None, None)),
        (0, 2, 3, (-1.5, None)),
    ],
)
def test__solve_square_equation__positive_solution_of_a_quadratic_level(square_coefficient, linear_coefficient, const_coefficient, expected):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected

@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient",
    [
        ("a", "b", "c"),
        ("a", "b", -1),
        ("a", -3, 3),
        (0, 2, "c"),
        (0, "b", "c"),
        ("a", 2, "c",)
    ],
)
def test__solve_square_equation__passing_a_string_as_an_argument_causes_a_TypeError(square_coefficient, linear_coefficient, const_coefficient):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

