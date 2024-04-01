import pytest
from faker import Faker
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize("text, good_words, bad_words, expected", [
    pytest.param(" ".join(Faker().words(nb=6, ext_word_list=["love", "happiness", "peace", "war", "pain", "death"], unique=True)),
    ["love", "happiness", "peace"], ["war", "pain", "death"], None, id="bad_words_and_good_words_equally"),
    pytest.param(" ".join(Faker().words(nb=5, ext_word_list=["love", "happiness", "peace", "war", "pain"], unique=True)),
    ["love", "happiness", "peace"], ["war", "pain", "death"], "GOOD", id="more_good_words_than_bad"),
    pytest.param(" ".join(Faker().words(nb=5, ext_word_list=["love", "happiness", "war", "pain", "death"], unique=True)),
    ["love", "happiness", "peace"], ["war", "pain", "death"], "BAD", id="more_bad_words_than_good"),
    pytest.param(" ".join(Faker().words(nb=6, ext_word_list=["love", "happiness", "peace", "war", "pain", "death"], unique=True)),
    [], [], None, id="lists_of_good_and_bad_words_are_empty")
])
def test__check_tweet_sentiment__emotional_colouring_of_text(text, good_words, bad_words, expected):
    result = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)
    assert result == expected






