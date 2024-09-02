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
    command_to_parse = []
    draw = False
    for i, command in enumerate(program, 1):
        result = COMMANDS[command[0]](command, draw)
        if isinstance(result, tuple):
            draw = result[1]
            result = result[0]
        command_to_parse.append(f'{i}. {result}')
    return command_to_parse

def pen_up(command, draw):
    ignored = ' (ignored)' if not draw else ''
    return f'PEN UP{ignored}', False
 

def pen_down(command, draw):
    ignored = ' (ignored)' if draw  else ''
    return f'PEN DOWN{ignored}', True

        
def pen_colour(command, draw):
    return f'P {command[1]}'


def move_north(command, draw):
    return format_direction_and_units(command, draw, "north")


def move_south(command, draw):
    return format_direction_and_units(command, draw, "south")


def move_east(command, draw):
    return format_direction_and_units(command, draw, "east")


def move_west(command, draw):
    return format_direction_and_units(command, draw, "west")


def format_string_for_singular_or_plural(command):
    return f'units' if int(command[1]) > 1 else 'unit'


def format_direction_and_units(command, draw, direction):
    action = 'Move' if draw == False else 'Draw a line'
    return f"{action} {command[1]} {format_string_for_singular_or_plural(command)} to the {direction}."
