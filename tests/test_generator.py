from gendiff.generator import generate_diff


def test_generate_diff_json():
    expected_output = open('tests/fixtures/result_json_1_2.txt').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected_output


def test_generate_diff_yaml():
    expected_output = open('tests/fixtures/result_yaml_1_2.txt').read()
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == expected_output


def test_generate_diff_is_string_json():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert type(result) == str


def test_generate_diff_is_string_yaml():
    result = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert type(result) == str


def test_generate_diff_json_rec():
    expected_output = open('tests/fixtures/result_json_3_4.txt').read()
    assert generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json') == expected_output


def test_generate_diff_plain():
    expected_output = open('tests/fixtures/result_plain.txt').read()
    assert generate_diff('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'plain') == expected_output


def test_generate_diff_is_string_plain():
    result = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'plain')
    assert type(result) == str


def test_generate_diff_json_is_string():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')
    assert type(result) == str
