from functions.level_1.five_title import change_copy_item


def test__change_copy_item__adds_text_copy_of_to_the_beginning():
    assert change_copy_item(title="test_string (100)") == "Copy of test_string (100)"

def test__change_copy_item__text_without_spaces_merging_with_a_number_in_round_brackets_is_deleted():
    assert change_copy_item(title="Copy of test_string(100)") == "Copy of (101)"

def test__change_copy_item__any_text_not_merging_with_a_number_in_round_brackets_will_not_be_deleted():
    assert change_copy_item(title="Copy of test_string (100)") == "Copy of test_string (101)"

def test__change_copy_item__deletes_the_last_word_in_the_text_merged_with_the_number_in_round_brackets():
    assert change_copy_item(title="Copy of test string(100)") == "Copy of test (101)"

def test__change_copy_item__the_number_in_round_brackets_is_incremented_by_one():
    assert change_copy_item(title="Copy of test string (100)") == "Copy of test string (101)"

def test__change_copy_item__ignores_the_number_in_curly_brackets_and_appended_with_2_in_round_brackets():
    assert change_copy_item(title="Copy of test string {100}") == "Copy of test string {100} (2)"

def test__change_copy_item__ignores_the_number_in_square_bracketed_and_appended_with_2_in_round_brackets():
    assert change_copy_item(title="Copy of test string [100]") == "Copy of test string [100] (2)"

def test__change_copy_item__ignores_adjacent_numbers_in_square_and_curly_brackets():
    assert change_copy_item(title="Copy of test string [99](100){99}") == "Copy of test string (101)"

def test__change_copy_item__text_equal_to_max_main_item_title_length_is_not_processed():
    assert change_copy_item(title="1" * 100) == "1" * 100

def test__change_copy_item__title_length_falls_within_the_allowed_range_of_maximum_length_and_adds_at_the_beginning_of_copy_of():
    assert change_copy_item(title="1" * 91) == f"Copy of {"1" * 91}"

def test__change_copy_item__title_length_does_not_falls_within_the_allowed_range_of_maximum_length():
    assert change_copy_item(title="1" * 92) == "1" * 92

