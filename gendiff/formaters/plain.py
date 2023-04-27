from gendiff.formaters.string_format import stringify_dict


def get_value_plain(value):
    if type(value) == dict:
        return '[complex value]'
    elif type(value) == str:
        return f"'{value}'"
    else:
        return stringify_dict(value)


def get_path_plain(previous_path, new_part):
    new_path = f'{previous_path}.{new_part}'[1:]
    return new_path


def gen_text_diff_plain_real(diff, path=''):
    result = ''
    for key in diff['keys']:
        if key in diff['removed'].keys():
            result += f"Property '{get_path_plain(path, key)}' was removed\n"
        elif key in diff['added'].keys():
            item = diff['added'][key]
            result += (f"Property '{get_path_plain(path, key)}' was added with"
                       f" value: {get_value_plain(item)}\n")
        elif key in diff['changed'].keys():
            if type(diff['changed'][key]) == dict:
                result += gen_text_diff_plain_real(diff['changed'][key],
                                                   path + f'.{key}')
            else:
                was = get_value_plain(diff['changed'][key][0])
                now = get_value_plain(diff['changed'][key][1])
                result += (f"Property '{get_path_plain(path, key)}' was "
                           f"updated. From {was} to {now}\n")
    return result


def gen_text_diff_plain(diff):
    plain_diff = gen_text_diff_plain_real(diff)
    return plain_diff[:len(plain_diff) - 1]
