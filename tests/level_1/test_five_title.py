import pytest
from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title,expected",
    [
        pytest.param("test_string (100)", "Copy of test_string (100)", id="adding_copy_of"),
        pytest.param(
            "Copy of test_string(100)",
            "Copy of (101)",
            marks=pytest.mark.xfail(
                reason="If the name is adjacent to a number in brackets deletes the name",
                run=True,
            ),
            id="file_name_removed",
        ),
        pytest.param(
            "Copy of test_string (100)",
            "Copy of test_string (101)",
            id="one_word_file_name_number_increased",
        ),
        pytest.param(
            "Copy of test string(100)",
            "Copy of test (101)",
            marks=pytest.mark.xfail(
                reason="Deletes the last word in the name if it is contiguous with the number",
                run=True,
            ),
            id="removed_part_of_the_name",
        ),
        pytest.param(
            "Copy of test string (100)",
            "Copy of test string (101)",
            id="few_word_file_name_number_increased",
        ),
        pytest.param(
            "Copy of test string {100}",
            "Copy of test string {100} (2)",
            id="ignore_curly_brackets_number_2_is_added",
        ),
        pytest.param(
            "Copy of test string [100]",
            "Copy of test string [100] (2)",
            id="ignore_square_brackets_number_2_is_added",
        ),
        pytest.param(
            "Copy of test string [99](100){99}",
            "Copy of test string (101)",
            id="the_number_has_been_extracted_and_enlarged",
        ),
        pytest.param("1" * 100, "1" * 100, id="100_character_name_is_ignored"),
        pytest.param("1" * 91, f"Copy of {'1' * 91}", id="91_character_name_processed"),
        pytest.param("1" * 92, "1" * 92, id="91_character_name_is_ignored"),
    ],
)
def test__change_copy_item__changes_name_and_number_in_the_title(title: str, expected: str) -> None:
    assert change_copy_item(title=title) == expected
