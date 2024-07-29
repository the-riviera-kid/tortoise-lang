import pytest

from tortoise_interpreter import (
    main_tortoise,
    sanitize_program,
    navigate_command_functions,
    pen_up,
    pen_down,
    pen_colour,
    get_pen_state,
    move_east,
    move_north
    )


def test_main_tortoise():
    program = [
        'P 2  # select pen 2',
        'D    # pen down',
        'W 2  # draw west 2cm',
        'N 1  # then north 1',
        'U    # pen up',
        'E 2  # move east 2',
        'S 1  # then back south',
        'D    # pen down',
        'N 1  # draw north 1',
    ]
    program = [list(i.strip()) for i in program]

    list_of_strings = []
    def print_function(stuff_to_print):
        list_of_strings.append(stuff_to_print)

    main_tortoise(program, print_function)

    assert list_of_strings == [
        '1. P 2',
        '2. PEN DOWN',
        '3. Draw a line 2 units to the west.',
        '4. Draw a line 1 unit to the north.',
        '5. PEN UP',
        '6. Move 2 units to the east.',
        '7. Move 1 unit to the south.',
        '8. PEN DOWN',
        '9. Draw a line 1 unit to the north.'
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

    COMMANDS = {'U': pen_up,'D': pen_down ,'P': pen_colour, 'N': move_north, 'E': move_east}
    program = [['P', '3'], ['U'], ['N', '1'], ['U'], ['D'], ['E', '2'], ['D']]
    command_to_parse = navigate_command_functions(COMMANDS, program)

    assert command_to_parse == ['1. P 3',
                                '2. PEN UP',
                                '3. Move 1 unit to the north.',
                                '4. PEN UP (ignored)',
                                '5. PEN DOWN',
                                '6. Draw a line 2 units to the east.',
                                '7. PEN DOWN (ignored)',
                                ]

def test_pen_up():
    assert pen_up(['U'], 'UP', 'DOWN') == 'PEN UP'

def test_pen_up_ignored():
    assert pen_up(['U'], 'UP', 'UP') == 'PEN UP (ignored)'

def test_pen_colour():
    assert pen_colour(['P', '2'], 'UP', '') == 'P 2'

def test_get_pen_state():
    assert get_pen_state(['D'], '') == 'DOWN'
