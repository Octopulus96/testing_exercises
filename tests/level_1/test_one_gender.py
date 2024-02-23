from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("run", "walk", "male") == "run"
    assert genderalize("run", "walk", "female") == "walk"
    assert genderalize("jump", "swim", "other") == "swim"