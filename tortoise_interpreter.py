def main_tortoise(program, print_to_screen=print):
    program = sanitize_program(program)
    COMMANDS = {'U': pen_up, 'D': pen_down, 'P': pen_colour, 'N': move_north, 'S': move_south, 'E': move_east, 'W': move_west}
    command_to_parse = navigate_command_functions(COMMANDS, program)

    for command in command_to_parse:
        print_to_screen(command)


def sanitize_program(program):
    # If a command has two parts, the second element of the list will be an empty string.
    # Remove this element. Then remove all elements after the first empty string in each list.
    # These were the comments at the end of each command.
    for command in program:
        if len(command) > 1:
            command.pop(1)
            if len(command) > 2:
                del command[command.index(' '):]
    return program


def navigate_command_functions(COMMANDS, program):
    # Comment
    return [f'{i}. {COMMANDS[command[0]](command)}' for i, command in enumerate(program, 1)]


def pen_up(command):
    return f'PEN UP'


def pen_down(command):
    return f'PEN DOWN'


def pen_colour(command):
    return f'P {command[1]}'


def move_north(command):
    return format_direction_and_units(command, "north")


def move_south(command):
    return format_direction_and_units(command, "south")


def move_east(command):
    return format_direction_and_units(command, "east")


def move_west(command):
    return format_direction_and_units(command, "west")


def format_string_for_singular_or_plural(command):
    return f'units' if int(command[1]) > 1 else 'unit'


def format_direction_and_units(command, direction):
    return f"Move {command[1]} {format_string_for_singular_or_plural(command)} to the {direction}."
