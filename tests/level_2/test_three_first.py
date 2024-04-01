import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize("items,default,expected_result", [
    pytest.param([1, 2, 3], "NOT_SET", 1, id="get_the_first_element_of_item_list"),
    pytest.param([], None, None, id="get_default_value"),
])
def test__first__argument_checking(items, default, expected_result):
    assert first(items, default) == expected_result

def test__first__item_is_an_empty_list_call_attribute_error():
    with pytest.raises(AttributeError):
        first(items=[])

