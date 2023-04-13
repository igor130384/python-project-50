import json


def generate_diff():
    with open('tests/fixtures/file1.json') as file:
        fileName1 = json.load(file)
    with open('tests/fixtures/file2.json') as file:
        fileName2 = json.load(file)
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
        return result
        #for key, v in result.items():
           # print(key, ':', v)