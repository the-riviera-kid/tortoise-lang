import pytest

from tortoise_interpreter import (
    main_tortoise,
    sanitize_program,
    navigate_command_functions,
    pen_up, pen_colour,
    )


def test_main_tortoise():
    program = [
        'P 2  # select pen 2',
        'D    # pen down',
        'W 2  # draw west 2cm',
        'N 1  # then north 1',
        'E 2  # then east 2',
        'S 1  # then back south',
        'U    # pen up'
    ]
    program = [list(i.strip()) for i in program]

    list_of_strings = []
    def print_function(stuff_to_print):
        list_of_strings.append(stuff_to_print)

    main_tortoise(program, print_function)

    assert list_of_strings == [
        '1. P 2',
        '2. PEN DOWN',
        '3. Move 2 units to the west.',
        '4. Move 1 unit to the north.',
        '5. Move 2 units to the east.',
        '6. Move 1 unit to the south.',
        '7. PEN UP'
    ]


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
