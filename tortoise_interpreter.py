def main_tortoise(program): 
    COMMANDS = {'U': pen_up, 'D': pen_down, 'P': pen_colour, 'N': move_north, 'S': move_south, 'E': move_east, 'W': move_west}
    command_to_parse = navigate_command_functions(COMMANDS, program)

    for command in command_to_parse:
        print(command)


def navigate_command_functions(COMMANDS, program):
    return [f'{i}. {COMMANDS[command[0]](command)}' for i, command in enumerate(program, 1)]


def pen_up(command):
    return f'PEN UP'


def pen_down(command):
    return f'PEN DOWN'


def pen_colour(command):
    return f'P {command[1]}'


def move_north(command):
    return f'N {command[1]}'


def move_south(command):
    return f'S {command[1]}'


def move_east(command):
    return f'E {command[1]}'


def move_west(command):
    return f'W {command[1]}'
