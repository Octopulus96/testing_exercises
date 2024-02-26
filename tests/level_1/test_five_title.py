from functions.level_1.five_title import change_copy_item


def test_change_copy_item_with_add_copy_of():
    assert change_copy_item(title="test_string (100)") == "Copy of test_string (100)"

def test_change_copy_snake_case_item_with_adjacent_number_in_round_brackets():
    assert change_copy_item(title="Copy of test_string(100)") == "Copy of (101)"

def test_change_copy_snake_case_item_with_number_in_round_brackets():
    assert change_copy_item(title="Copy of test_string (100)") == "Copy of test_string (101)"

def test_change_copy_item_with_adjacent_number_in_round_brackets():
    assert change_copy_item(title="Copy of test string(100)") == "Copy of test (101)"

def test_change_copy_item_with_number_in_round_brackets():
    assert change_copy_item(title="Copy of test string (100)") == "Copy of test string (101)"

def test_change_copy_item_with_number_in_curly_brackets():
    assert change_copy_item(title="Copy of test string {100}") == "Copy of test string {100} (2)"

def test_change_copy_item_with_number_square_bracketed():
    assert change_copy_item(title="Copy of test string [100]") == "Copy of test string [100] (2)"

def test_change_copy_item_with_number_round_bracketed_alongside_the_other_brackets():
    assert change_copy_item(title="Copy of test string [99](100){99}") == "Copy of test string (101)"

def test_change_copy_item_title_length_is_too_much():
    assert change_copy_item(title="1" * 100) == "1" * 100

def test_change_copy_item_title_length_is_normal():
    assert change_copy_item(title="1" * 91) == f"Copy of {"1" * 91}"

def test_change_copy_item_title_length_is_beyond():
    assert change_copy_item(title="1" * 92) == "1" * 92

