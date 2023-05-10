from gendiff.formaters.json import diff_json
from gendiff.formaters.plain import format
from gendiff.formaters.stylish import stylish


def get_format(string_format):
    if string_format == 'stylish' or not string_format:
        return stylish
    elif string_format == 'plain':
        return format
    elif string_format == 'json':
        return diff_json
    else:
        raise Exception('Error! Wrong output format')
