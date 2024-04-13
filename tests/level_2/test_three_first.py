import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        pytest.param([1, 2, 3], "NOT_SET", 1, id="get_the_first_element_of_item_list"),
        pytest.param([], None, None, id="get_default_None"),
        pytest.param([], 1, 1, id="get_default_int"),
        pytest.param([], "string", "string", id="get_default_string"),
    ],
)
def test__first__argument_checking(
    items: list[int], default: int | None | str, expected_result: int | None | str
) -> None:
    assert first(items, default) == expected_result


def test__first__item_is_an_empty_list_and_default_NOT_SET_call_attribute_error() -> None:
    with pytest.raises(AttributeError):
        first(items=[])
