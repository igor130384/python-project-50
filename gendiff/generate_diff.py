from gendiff.data import data_form
from gendiff.formatter import get_format
from gendiff.parser import parse


def gen_different(item1, item2):
    if type(item1) == dict and type(item2) == dict:
        return gen_base_diff(item1, item2)
    else:
        return item1, item2


def gen_base_diff(dict1, dict2):
    diff = {
        'unchanged': {},
        'removed': {},
        'added': {},
        'changed': {},
        'nested': {},
        'keys': []
    }
    keys = list(set(dict1.keys()).union(set(dict2.keys())))
    diff['keys'].extend(keys)
    for key in keys:
        if dict1.get(key) == dict2.get(key):
            diff['unchanged'][key] = dict1.get(key)
        elif key in dict1.keys() and key not in dict2.keys():
            diff['removed'][key] = dict1.get(key)
        elif key not in dict1.keys() and key in dict2.keys():
            diff['added'][key] = dict2.get(key)
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff['nested'][key] = gen_different(dict1[key], dict2[key])
        else:
            diff['changed'][key] = {
                'old_value': dict1[key],
                'new_value': dict2[key]
            }

    diff['keys'].sort()
    return diff


def generate_diff(file_path1, file_path2, format='stylish'):
    data1, format1 = data_form(file_path1)
    data2, format2 = data_form(file_path2)
    file1 = parse(data1, format1)
    file2 = parse(data2, format2)
    return get_format(format)(gen_base_diff(file1, file2))


