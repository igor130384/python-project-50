from gendiff.choose_format import get_choose
from gendiff.compare_format import definition_form
from gendiff.generate_diff import gen_base_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    decorator = get_choose(format)
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    return decorator(gen_base_diff(file1, file2))
