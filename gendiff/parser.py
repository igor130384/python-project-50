import json

import yaml


def parse(data: str, format: str) -> dict:
    if format == "json":
        return json.loads(data)
    elif format == "yaml" or format == "yml":
        return yaml.safe_load(data)
    else:
        raise Exception('Error! Wrong output format')
