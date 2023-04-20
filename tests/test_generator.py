from gendiff.generator import generate_diff


def test_generate_diff_json():
    expected_output = '{\n' '- follow: False\n''  host: hexlet.io\n' \
                      '- proxy: 123.234.53.22\n' \
                      '- timeout: 50\n''+ timeout: 20\n' \
                      '+ verbose: True \n''}'
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected_output


def test_generate_diff_yaml():
    expected_output = '{\n' '- follow: False\n''  host: hexlet.io\n' \
                      '- proxy: 123.234.53.22\n' \
                      '- timeout: 50\n''+ timeout: 20\n' \
                      '+ verbose: True \n''}'
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == expected_output


def test_generate_diff_is_string_json():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert type(result) == str


def test_generate_diff_is_string_yaml():
    result = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert type(result) == str
