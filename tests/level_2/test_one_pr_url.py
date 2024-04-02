import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url, expected",
    [
        pytest.param(
            "https://github.com/user/repo/pull/1", True, id="url_is_github_pull_request"
        ),
        pytest.param(
            "https://gitlab.com/user/repo/merge_requests/1",
            False,
            id="url_does_not_lead_to_pull_request",
        ),
        pytest.param(
            "https://bitbucket.org/user/repo/pull-requests/1",
            False,
            id="url_does_not_lead_to_github",
        ),
    ],
)
def test__is_github_pull_request_url(url: str, expected: bool):
    assert is_github_pull_request_url(url=url) == expected
