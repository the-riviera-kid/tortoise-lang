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
    pen_state = ''
    for i, command in enumerate(program, 1):
        result = COMMANDS[command[0]](command, pen_state)
        if isinstance(result, tuple):
            pen_state = result[1]
            result = result[0]
        command_to_parse.append(f'{i}. {result}')
    return command_to_parse

def pen_up(command, pen_state):
    if pen_state == "DOWN" or pen_state == '':
        pen_state = "UP"
        return f'PEN UP', pen_state
    return f'PEN UP (ignored)', pen_state


def pen_down(command, pen_state):
    if pen_state == "UP" or pen_state == '':
        pen_state = "DOWN"
        return f'PEN DOWN', pen_state
    return f'PEN DOWN (ignored)', pen_state

        
def pen_colour(command, pen_state):
    return f'P {command[1]}'


def move_north(command, pen_state):
    return format_direction_and_units(command, pen_state, "north")


def move_south(command, pen_state):
    return format_direction_and_units(command, pen_state, "south")


def move_east(command, pen_state):
    return format_direction_and_units(command, pen_state, "east")


def move_west(command, pen_state):
    return format_direction_and_units(command, pen_state, "west")


def format_string_for_singular_or_plural(command):
    return f'units' if int(command[1]) > 1 else 'unit'


def format_direction_and_units(command, pen_state, direction):
    action = 'Move' if pen_state == 'UP' else 'Draw a line'
    return f"{action} {command[1]} {format_string_for_singular_or_plural(command)} to the {direction}."
