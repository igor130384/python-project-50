import json


def generate_diff(filename1, filename2):
    with open(filename1) as json_file:
        fileName1 = json.load(json_file)
    with open(filename2) as json_file:
        fileName2 = json.load(json_file)
    result = {}
    for key in fileName1:
        if key in fileName2 and fileName1[key] == fileName2[key]:
            result['  ' + key] = fileName1[key]
            del fileName2[key]
        elif key in fileName2 and fileName1[key] != fileName2[key]:
            result['- ' + key] = fileName1[key]
            result['+ ' + key] = fileName2[key]
            del fileName2[key]
        else:
            result['- ' + key] = fileName1[key]
    for key, v in fileName2.items():
        fileName2_new = {'+ ' + key: v}
        result.update(fileName2_new)
        result = dict(sorted(result.items(), key=lambda x: x[0][2]))
        s = '\n'.join(f'{k}: {v}' for k, v in result.items())
        return result


#print(generate_diff('file1.json', 'file2.json'))

# for key, v in result.items():
# print(key, ':', v)
# print('}')
