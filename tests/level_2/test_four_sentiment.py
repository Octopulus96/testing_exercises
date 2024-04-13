import random
from typing import Set, List
import pytest
from faker import Faker
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.fixture(name="random_text_with_unique_words")
def fixture_random_text() -> str:
    def factory(ext_word_set: Set[str]) -> str:
        fake = Faker()
        text = fake.text(200)
        text_list: List[str] = text.split()
        text_list = [word.lower() for word in text_list if word not in ext_word_set]
        for word in ext_word_set:
            random_index = random.randint(0, len(text_list))
            text_list.insert(random_index, word)
        modified_text = " ".join(text_list)
        return modified_text

    return factory


@pytest.mark.parametrize(
    "good_words, bad_words, expected",
    [
        pytest.param(
            {"love", "happiness", "peace"},
            {"war", "pain", "death"},
            None,
            id="bad_words_and_good_words_equally",
        ),
        pytest.param(
            {"love", "happiness", "peace"},
            {"war", "pain"},
            "GOOD",
            id="more_good_words_than_bad",
        ),
        pytest.param(
            {"love", "happiness"},
            {"war", "pain", "death"},
            "BAD",
            id="more_bad_words_than_good",
        ),
    ],
)
def test__check_tweet_sentiment__emotional_colouring_of_text(
    random_text_with_unique_words: str, good_words: Set[str], bad_words: Set[str], expected: str | None
) -> None:
    text = random_text_with_unique_words(good_words | bad_words)
    result = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)
    assert result == expected


def test__check_tweet_sentiment__lists_of_good_and_bad_words_are_empty(
    random_text_with_unique_words: str,
) -> None:
    text = random_text_with_unique_words(set())
    result = check_tweet_sentiment(
        text=text, good_words={"love", "happiness", "peace"}, bad_words={"war", "pain", "death"}
    )
    assert result is None
