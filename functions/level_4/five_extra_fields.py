import configparser
from typing import Mapping


def fetch_extra_fields_configuration(config_file_path: str) -> Mapping[str, type]:
    config = configparser.ConfigParser()
    config.read(config_file_path)
    raw_extra_fields_config = fetch_app_config_field(config_file_path, "extra_fields")
    return (
        {
            line.split(": ")[0]: eval(line.split(": ")[1])
            for line in raw_extra_fields_config.strip().split("\n")
        }
        if raw_extra_fields_config
        else {}
    )


def fetch_app_config_field(config_file_path: str, field_name: str) -> str | None:
    config = configparser.ConfigParser()
    config.read(config_file_path)
    try:
        return config["tool:app-config"][field_name]
    except KeyError:
        return None
