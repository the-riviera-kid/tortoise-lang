import pytest

from tortoise_interpreter import (
    sanitize_program,
    navigate_command_functions,
    pen_up, pen_colour,
    )


@pytest.mark.parametrize('program,                         expected', [
    (['P 3', 'U', 'D'],                                    [['P', '3'], ['U'], ['D']]),
    (['P 3', 'U', 'D', 'P 3', 'U', 'D'],                   [['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D']]),
    ([ 'P 3', 'U', 'D', 'P 3', 'U', 'D', 'P 3', 'U', 'D'], [['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D']]),
    ([
        'P 2  # select pen 2',
        'D    # pen down',
        'W 2  # draw west 2cm',
        'N 1  # then north 1',
        'E 2  # then east 2',
        'S 1  # then back south',
        'U    # pen up'
    ],                                                     [['P', '2'], ['D'], ['W', '2'], ['N', '1'], ['E', '2'], ['S', '1'], ['U']]),
])
def test_sanitized_programs(program, expected):
    program = [list(i.strip()) for i in program]
    sanitized_program = sanitize_program(program)
    assert sanitized_program == expected


def test_navigate_command_functions():
    def pen_up(command):
        return f'PEN UP'
    
    def pen_colour(command):
        return f'P {command[1]}'

    COMMANDS = {'U': pen_up, 'P': pen_colour}
    program = [['P', '3'], ['U']]
    command_to_parse = navigate_command_functions(COMMANDS, program)

    assert command_to_parse == ['1. P 3', '2. PEN UP']


def test_pen_up():
    assert pen_up(['U']) == 'PEN UP'


def test_pen_colour():
    assert pen_colour(['P', '2']) == 'P 2'
