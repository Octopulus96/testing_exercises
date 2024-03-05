import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__returns_True_on_getting_the_github_link_to_poolrequest():
    assert is_github_pull_request_url("https://github.com/user/repo/pull/1") == True

def test__is_github_pull_request_url__returns_False_on_getting_the_githab_link_not_leading_to_poolrequest():
    assert is_github_pull_request_url("https://gitlab.com/user/repo/merge_requests/1") == False

def test__is_github_pull_request_url__returns_False_on_getting_a_link_not_githab():
    assert is_github_pull_request_url("https://bitbucket.org/user/repo/pull-requests/1") == False

def test__is_github_pull_request_url__when_passing_url_not_of_string_type_it_returns_AttributeError():
    with pytest.raises(AttributeError):
        is_github_pull_request_url(1)