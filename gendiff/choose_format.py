from gendiff.formaters.json import diff_json
from gendiff.formaters.plain import gen_text_diff_plain
from gendiff.formaters.stylish import stylish


def get_choose(decorator):
    if decorator == 'stylish' or not decorator:
        decorator = stylish
    elif decorator == 'plain':
        decorator = gen_text_diff_plain
    elif decorator == 'json':
        decorator = diff_json
    else:
        raise Exception('Error! Wrong output format')
    return decorator
