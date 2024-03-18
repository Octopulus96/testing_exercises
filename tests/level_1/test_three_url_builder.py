from functions.level_1.three_url_builder import build_url


def test__build_url__with_only_path():
    assert build_url("https://example.com", "api/data") == "https://example.com/api/data"

def test__build_url__with_path_and_many_params():
    assert build_url("https://example.com", "api/data", {"param1": "value1", "param2": "value2"}) == "https://example.com/api/data?param1=value1&param2=value2"

def test__build_url__with_path_and_empty_params():
    assert build_url("https://example.com", "api/data", {}) == "https://example.com/api/data"

def test__build_url__with_path_and_few_params():
    assert build_url("https://example.com", "api/data", {"param": "value"}) == "https://example.com/api/data?param=value"

