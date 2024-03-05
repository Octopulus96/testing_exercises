import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment

@pytest.fixture
def sample_text_data():
    return {
        "non_triggered_text": """Likewise, the current structure of the organisation requires the definition
        and refinement of new proposals. The task of the organisation, especially the consultation
        with the broader asset base, is largely responsible for the establishment of a training
        system that is in line with immediate needs.""",

        "text_with_balanced_good_and_bad_words": """Love and happiness once filled the hearts of people,
    but peace was disturbed by war and pain. Joy and kindness became rare treasures,
    while death and war left their mark on the earth. Hatred and evil took hold of the souls,
    and the world became a shadow of its former beauty.""",

        "good_words": ["love", "happiness", "peace"],
        "bad_words": ["war", "pain", "death"]
    }

def test__check_tweet_sentiment__returns_BAD_list_of_bad_words_more_than_good_words(sample_text_data):
    good_words = sample_text_data["good_words"]

    result = check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                                   good_words=good_words.pop(),
                                   bad_words=sample_text_data["bad_words"])
    assert result == "BAD"

def test__check_tweet_sentiment__returns_GOOD_list_of_good_words_more_than_bad_words(sample_text_data):
    bad_words = sample_text_data["bad_words"]
    
    result = check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                                   good_words=sample_text_data["good_words"],
                                   bad_words=bad_words.pop())
    assert result == "GOOD"

def test__check_tweet_sentiment__there_is_an_equal_balance_of_bad_and_good_words_in_the_text(sample_text_data):
    result = check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                                   good_words=sample_text_data["good_words"],
                                   bad_words=sample_text_data["bad_words"])
    assert result == None

def test__check_tweet_sentiment__if_both_lists_are_empty_returns_None(sample_text_data):
    result = check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                                   good_words=[],
                                   bad_words=[])
    assert result == None

def test__check_tweet_sentiment__there_is_an_equal_balance_of_bad_and_good_words_in_the_text(sample_text_data):
    result = check_tweet_sentiment(text=sample_text_data["non_triggered_text"],
                                   good_words=sample_text_data["good_words"],
                                   bad_words=sample_text_data["bad_words"])    
    assert result == None

def test__check_tweet_sentiment__returns_None_if_type_of_word_list_arguments_are_iterable_set(sample_text_data):
    result = check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                                   good_words={},
                                   bad_words=())
    assert result == None

def test__check_tweet_sentiment__сauses_a_TypeError_exception_if_bad_words_is_not_an_iterated_number(sample_text_data):
    with pytest.raises(TypeError):
        check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                              good_words=sample_text_data["good_words"],
                              bad_words=1)
        
def test__check_tweet_sentiment__сauses_a_TypeError_exception_if_good_words_is_not_an_iterated_number(sample_text_data):
    with pytest.raises(TypeError):
        check_tweet_sentiment(text=sample_text_data["text_with_balanced_good_and_bad_words"],
                              good_words=1,
                              bad_words=sample_text_data["bad_words"])

def test__check_tweet_sentiment__if_the_argument_text_not_str_raises_an_AttributeError_exception(sample_text_data):
    with pytest.raises(AttributeError):
        check_tweet_sentiment(text=1,
                              good_words=sample_text_data["good_words"],
                              bad_words=sample_text_data["bad_words"])