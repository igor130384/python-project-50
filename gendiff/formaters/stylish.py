from gendiff.formaters.string_format import stringify_dict


def gen_tree_changed(item, key, depth):
    result = ''
    if type(item) == dict:
        result += (f'{depth * "    "}{key}: '
                   f'{stylish(item, depth + 1)}\n')
    else:
        item1 = stringify_dict(item[0], depth + 1)
        item2 = stringify_dict(item[1], depth + 1)
        result += f'{(depth - 1) * "    "}  - {key}: {item1}\n'
        result += f'{(depth - 1) * "    "}  + {key}: {item2}\n'
    return result


def stylish(diff, depth=1):
    result = ''
    for key in diff['keys']:
        if key in diff['unchanged'].keys():
            item = stringify_dict(diff["unchanged"][key], depth + 1)
            result += f'{depth * "    "}{key}: {item}\n'
        elif key in diff['removed'].keys():
            item = stringify_dict(diff["removed"][key], depth + 1)
            result += f'{(depth - 1) * "    "}  - {key}: {item}\n'
        elif key in diff['added'].keys():
            item = stringify_dict(diff["added"][key], depth + 1)
            result += f'{(depth - 1) * "    "}  + {key}: {item}\n'
        elif key in diff['changed'].keys():
            item = diff['changed'][key]
            result += gen_tree_changed(item, key, depth)
    result = '{\n' + result + f'{(depth - 1) * "    "}' + '}'
    return result
