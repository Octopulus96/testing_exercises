import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "masculine,feminine,gender,expected",
    [
        pytest.param(
            "ходил", "ходила", "male", "ходил", id="return_male_verb_for_male_gender"
        ),
        pytest.param(
            "ходил",
            "ходила",
            "female",
            "ходила",
            id="return_female_verb_for_female_gender",
        ),
        pytest.param(
            "ходил",
            "ходила",
            "other",
            "ходила",
            id="return_female_verb_for_other_gender",
        ),
    ],
)
def test__genderalize__recognise_gender_based_on_sex(
    masculine: str, feminine: str, gender: str, expected: str
) -> None:
    assert genderalize(masculine, feminine, gender) == expected
