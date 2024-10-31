# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest

from tortoise_interpreter import (
    main_tortoise,
    sanitize_program,
    navigate_command_functions,
)


def test_main_tortoise():
    program = [
        "P 2  # select pen 2",
        "D    # pen down",
        "W 2  # draw west 2cm",
        "U    # pen up",
        "E 2  # move east 2",
    ]
    program = [list(i.strip()) for i in program]

    list_of_strings = []

    def print_function(stuff_to_print):
        list_of_strings.append(stuff_to_print)

    main_tortoise(program, "shityfilename", False, print_function)

    assert list_of_strings == [
        "1. P 2",
        "2. PEN DOWN",
        "3. Draw a line 2 units to the west.",
        "4. PEN UP",
        "5. Move 2 units to the east.",
    ]


def test_main_tortoise_verbose():
    program = [
        "P 2  # select pen 2",
        "D    # pen down",
        "W 2  # draw west 2cm",
    ]
    program = [list(i.strip()) for i in program]

    list_of_strings = []

    def print_function(stuff_to_print):
        list_of_strings.append(stuff_to_print)

    main_tortoise(program, "shityfilename", True, print_function)

    assert list_of_strings == [
        "\nExecuting shityfilename, 3 commands found\n",
        "1. P 2",
        "2. PEN DOWN",
        "3. Draw a line 2 units to the west.",
    ]


# fmt: off
@pytest.mark.parametrize('program,                         expected', [
    (['P 3', 'U', 'D'],                                   [['P', '3'], ['U'], ['D']]),
    # pylint: disable=line-too-long
    (['P 3', 'U', 'D', 'P 3', 'U', 'D'],                  [['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D']]),
    (['P 3', 'U', 'D', 'P 3', 'U', 'D', 'P 3', 'U', 'D'], [['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D']]),
    ([
        'P 2  # select pen 2',
        'D    # pen down',
        'W 2  # draw west 2cm',
        'N 1  # then north 1',
        'E 2  # then east 2',
        'S 1  # then back south',
        'U    # pen up'
    ],                                                    [['P', '2'], ['D'], ['W', '2'], ['N', '1'], ['E', '2'], ['S', '1'], ['U']]),
    # pylint: enable=line-too-long
])
# fmt: on
def test_sanitized_programs(program, expected):
    program = [list(i.strip()) for i in program]
    sanitized_program = sanitize_program(program)
    assert sanitized_program == expected


def test_navigate_command_functions():
    def underscore(_, pen_state):
        return ("___", pen_state), pen_state

    def double_colon(_, pen_state):
        return "::", pen_state

    def hard_stop(commands, pen_state):
        factor = int(commands[1])
        return "." * factor, pen_state

    commands = {"U": underscore, "D": double_colon, "H": hard_stop}
    program = [["U"], ["D"], ["H", "4"]]
    command_to_parse = navigate_command_functions(commands, program)

    assert command_to_parse == [
        "1. ('___', 'Move')",
        "2. ::",
        "3. ....",
    ]
