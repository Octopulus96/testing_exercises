import pytest

from functions.level_2.three_first import first

@pytest.fixture
def sample_first_items():
    return {
        "empty_list": [],  
        "empty_dict": {}, 
        "int_list": [1, 2, 3],
        "int_tuple": (1, 2, 3),
        "str_list": ["a", "b", "c"],
        "str_tuple": ("a","b", "c"),
        "str_dict": {"1":"1", "2":"2"},
        "default_int" : 0,
        "defautl_None" : None,
        "default_str" : "something",
        "NON_SET": "NON_SET"
    }


def test__first__returns_the_first_item_in_the_item_list(sample_first_items):
    assert first(sample_first_items["int_list"]) == 1

def test__first__returns_the_first_item_tuple(sample_first_items):
    assert first(sample_first_items["int_tuple"]) == 1

def test__first__returns_the_first_item_of_item_list_of_string_type(sample_first_items):
    assert first(sample_first_items["str_list"], sample_first_items["default_int"]) == "a"

def test__first__returns_the_first_item_tuple_of_the_string_type(sample_first_items):
    assert first(sample_first_items["str_tuple"], sample_first_items["default_int"]) == "a"

def test__first__returns_int_value_default_if_list_item_is_empty(sample_first_items):
    assert first(sample_first_items["empty_list"], sample_first_items["default_int"]) == 0

def test__first__returns_int_to_default_if_dict_item_is_empty(sample_first_items):
    assert first(sample_first_items["empty_dict"], sample_first_items["default_int"]) == 0

def test__first__returns_None_default_value_if_list_item_is_empty(sample_first_items):
    assert first(sample_first_items["empty_list"], sample_first_items["defautl_None"]) == None

def test__first__returns_string_default_if_list_item_is_empty(sample_first_items):
    assert first(sample_first_items["empty_list"], sample_first_items["default_str"]) == "something"

def test__first__dict_passed_to_the_item_argument_raises_a_KeyError_exception(sample_first_items):
    with pytest.raises(KeyError):
        first(sample_first_items["str_dict"], sample_first_items["default_int"]) 

def test__first__passing_item_to_an_empty_list_and_passing_nothing_to_default_raises_an_AttributeError_exception(sample_first_items):
    with pytest.raises(AttributeError):
        first(sample_first_items["empty_list"])

def test__first__passing_item_to_an_empty_list_and_default_NOT_SET_raises_an_AttributeError_exception(sample_first_items):
    with pytest.raises(AttributeError):
        first(sample_first_items["empty_list"], default=sample_first_items["NOT_SET"])