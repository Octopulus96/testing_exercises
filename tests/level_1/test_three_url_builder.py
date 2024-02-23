from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("https://example.com", "api/data") == "https://example.com/api/data"
    assert build_url("https://example.com", "api/data", {"param1": "value1", "param2": "value2"}) == "https://example.com/api/data?param1=value1&param2=value2"
    assert build_url("https://example.com", "api/data", {}) == "https://example.com/api/data"
    assert build_url("https://example.com", "api/data", {"param": "value"}) == "https://example.com/api/data?param=value"

