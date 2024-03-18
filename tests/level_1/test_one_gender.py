from functions.level_1.one_gender import genderalize


def test__generalize__return_male_verb_for_male_gender():
    assert genderalize("ходил", "ходила", "male") == "ходил"

def test__generalize__return_female_verb_for_female_gender():
    assert genderalize("ходил", "ходила", "female") == "ходила"

def test__genderalize__return_female_verb_for_unknown_gender():
    assert genderalize("ходил", "ходила", "other") == "ходила"