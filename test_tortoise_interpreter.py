from tortoise_interpreter import (
    sanitize_program,
    navigate_command_functions,
    pen_up, pen_colour,
    )


def test_sanatize_program_tiny_tortoise():
    sanitized_program = sanitize_program([['P', ' ', '3'], ['U'], ['D']])
    assert sanitized_program == [['P', '3'], ['U'], ['D']]


def test_sanatize_program_medium_tortoise():
    sanitized_program = sanitize_program([['P', ' ', '3'], ['U'], ['D'], ['P', ' ', '3'], ['U'], ['D']])
    assert sanitized_program == [['P', '3'], ['U'], ['D'], ['P', '3'], ['U'], ['D']]


def test_sanatize_program_example_tortoise():
    sanitized_program = sanitize_program(
        [
            ['P', ' ', '2', ' ', ' ', '#', ' ', 's', 'e', 'l', 'e', 'c', 't', ' ', 'p', 'e', 'n', ' ', '2'],
            ['D', ' ', ' ', ' ', ' ', '#', ' ', 'p', 'e', 'n', ' ', 'd', 'o', 'w', 'n'],
            ['W', ' ', '2', ' ', ' ', '#', ' ', 'd', 'r', 'a', 'w', ' ', 'w', 'e', 's', 't', ' ', '2', 'c', 'm'],
            ['N', ' ', '1', ' ', ' ', '#', ' ', 't', 'h', 'e', 'n', ' ', 'n', 'o', 'r', 't', 'h', ' ', '1'],
            ['E', ' ', '2', ' ', ' ', '#', ' ', 't', 'h', 'e', 'n', ' ', 'e', 'a', 's', 't', ' ', '2'],
            ['S', ' ', '1', ' ', ' ', '#', ' ', 't', 'h', 'e', 'n', ' ', 'b', 'a', 'c', 'k', ' ', 's', 'o', 'u', 't', 'h'],
            ['U', ' ', ' ', ' ', ' ', '#', ' ', 'p', 'e', 'n', ' ', 'u', 'p']
        ]
    )
    assert sanitized_program == [['P', '2'], ['D'], ['W', '2'], ['N', '1'], ['E', '2'], ['S', '1'], ['U']]


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
