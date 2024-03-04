import pytest
from functions.level_2.five_replace_word import replace_word

@pytest.fixture
def sample_strings():
    return {
        "empty_string": "",
        "text": "Съешь ещё этих мягких французских булок, да выпей же чаю",
        "expected_result": "Съешь ещё этих мягких английских булок, да выпей же чаю",
        "replace_from": "французских",
        "replace_to": "английских",
        "replace_not_found": "немецких",
        "number": 1
    }

def test__relace_word__word_was_found_in_the_text_and_replaced_with_another_word(sample_strings):
    result = replace_word(text=sample_strings["text"],
                          replace_from=sample_strings["replace_from"],
                          replace_to=sample_strings["replace_to"])

    assert result == sample_strings["expected_result"]

def test__relace_word__text_returns_unchanged_if_replace_from_is_not_in_the_text(sample_strings):
    result = replace_word(text=sample_strings["text"],
                          replace_from=sample_strings["replace_not_found"],
                          replace_to=sample_strings["replace_to"])
    
    assert result == sample_strings["text"]

def test__relace_word__when_an_empty_string_is_received_in_the_text_argent_returns_an_empty_string(sample_strings):
    result = replace_word(text=sample_strings["empty_string"],
                          replace_from=sample_strings["replace_not_found"],
                          replace_to=sample_strings["replace_to"])
    
    assert result == sample_strings["empty_string"]

def test__relace_word__getting_int_in_replace_from_returns_AttributeError_exception(sample_strings):
    with pytest.raises(AttributeError):
        replace_word(text=sample_strings["text"],
                     replace_from=sample_strings["number"],
                     replace_to=sample_strings["replace_to"])

def test__relace_word__when_getting_int_in_replace_to_it_returns_TypeError_exception(sample_strings):
    with pytest.raises(TypeError):
        replace_word(text=sample_strings["text"],
                     replace_from=sample_strings["replace_from"],
                     replace_to=sample_strings["number"])