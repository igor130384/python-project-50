from gendiff.formaters.json import diff_json
from gendiff.formaters.plain import format
from gendiff.formaters.stylish import stylish


def get_format(decorator):
    if decorator == 'stylish' or not decorator:
        decorator = stylish
    elif decorator == 'plain':
        decorator = format
    elif decorator == 'json':
        decorator = diff_json
    else:
        raise Exception('Error! Wrong output format')
    return decorator
