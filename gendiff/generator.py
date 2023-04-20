from gendiff.compare_format import definition_form


def generate_diff(filename1, filename2):
    file_dict1 = definition_form(filename1)
    file_dict2 = definition_form(filename2)
    result = {}
    for key in file_dict1:
        if key in file_dict2 and file_dict1[key] == file_dict2[key]:
            result['  ' + key] = file_dict1[key]
            del file_dict2[key]
        elif key in file_dict2 and file_dict1[key] != file_dict2[key]:
            result['- ' + key] = file_dict1[key]
            result['+ ' + key] = file_dict2[key]
            del file_dict2[key]
        else:
            result['- ' + key] = file_dict1[key]
    for key, v in file_dict2.items():
        file_dict2_new = {'+ ' + key: v}
        result.update(file_dict2_new)
        result = dict(sorted(result.items(), key=lambda x: x[0][2]))
        s = "{\n" + '\n'.join(f'{k}: {v}' for k, v in result.items()) + ' \n}'
    return s
