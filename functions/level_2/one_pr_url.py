def is_github_pull_request_url(url: str) -> bool:
    splitted_url = url.split("/")
    return (
        len(splitted_url) == 7
        and splitted_url[2] == "github.com"
        and splitted_url[5] == "pull"
    )
