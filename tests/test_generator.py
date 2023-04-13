
from gendiff.scripts.generator import generate_diff


def test_generate_diff():
    expected_output = {'- follow': False,
                       '  host': 'hexlet.io',
                       '- proxy': '123.234.53.22',
                       '- timeout': 50,
                       '+ timeout': 20, '+ verbose': True}
    assert generate_diff() == expected_output
