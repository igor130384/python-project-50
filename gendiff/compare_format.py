import json

import yaml


def definition_form(file_path):
    f = open(file_path)
    if file_path[-4:] == "json":
        return dict((json.load(f)))
    elif file_path[-4:] == "yaml" or file_path[-3:] == "yml":
        return dict((yaml.safe_load(f)))
    else:
        raise ValueError('Unsupported format. '
                         'Next formats are supported: .json .yaml .yml')
