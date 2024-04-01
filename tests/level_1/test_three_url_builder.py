import pytest
from functions.level_1.three_url_builder import build_url

@pytest.mark.parametrize("base_url,path,params,expected", [
    pytest.param("https://example.com", "api/data", None, "https://example.com/api/data", id="with_only_path"),
    pytest.param("https://example.com", "api/data", {"param1": "value1", "param2": "value2"}, "https://example.com/api/data?param1=value1&param2=value2", id="with_path_and_many_params"),
    pytest.param("https://example.com", "api/data", {}, "https://example.com/api/data", id="with_path_and_empty_params"),
    pytest.param("https://example.com", "api/data", {"param": "value"}, "https://example.com/api/data?param=value", id="with_path_and_few_params"),
])
def test__build_url__generate_a_url_string(base_url, path, params, expected):
    assert build_url(base_url, path, params) == expected
