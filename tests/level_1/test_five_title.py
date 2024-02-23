from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    title = {
        0: "test_string (100)",
        1: "Copy of test_string(100)",
        2: "Copy of test string(100)",
        3: "Copy of test_string (100)",
        4: "Copy of test string (100)",
        5: "Copy of test string {100}",
        6: "Copy of test string [100]",
        7: "Copy of test string [99](100){99}",
        8: "1" * 100,
        9: "1" * 91,
        10: "1" * 92
    }
    assert change_copy_item(title=title[0]) == "Copy of test_string (100)"
    assert change_copy_item(title=title[1]) == "Copy of (101)"
    assert change_copy_item(title=title[2]) == "Copy of test (101)"
    assert change_copy_item(title=title[3]) == "Copy of test_string (101)"
    assert change_copy_item(title=title[4]) == "Copy of test string (101)"
    assert change_copy_item(title=title[5]) == "Copy of test string {100} (2)"
    assert change_copy_item(title=title[6]) == "Copy of test string [100] (2)"
    assert change_copy_item(title=title[7]) == "Copy of test string (101)"
    assert change_copy_item(title=title[8]) == title[8]
    assert change_copy_item(title=title[9]) == f"Copy of {title[9]}"
    assert change_copy_item(title=title[10]) == title [10]
