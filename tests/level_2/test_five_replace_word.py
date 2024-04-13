import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text,replace_from,replace_to,expected",
    [
        pytest.param(
            "replace_from test text",
            "replace_from",
            "replace_to",
            "replace_to test text",
            id="word_is_replaced",
        ),
        pytest.param(
            "", "replace_from", "replace_to", "", id="empty_string_is_ignored"
        ),
        pytest.param(
            "something test text",
            "replace_from",
            "replace_to",
            "something test text",
            id="word_is_not_in_the_text",
        ),
    ],
)
def test__replace_word__replaces_word_in_text(
    text: str, replace_from: str, replace_to: str, expected: str
) -> None:
    result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)
    assert result == expected
