"""Implementation of tortoise-language."""

MOVE = "Move"
DRAW = "Draw a line"


def main_tortoise(program, filename, verbose, print_to_screen=print):
    """Main function that interprets a tortoise program."""
    program = sanitize_program(program)
    commands = {
        "U": pen_up,
        "D": pen_down,
        "P": pen_colour,
        "N": move_north,
        "S": move_south,
        "E": move_east,
        "W": move_west,
    }
    command_to_parse = navigate_command_functions(commands, program)

    if verbose:
        print_to_screen(f"Executing {filename}, {len(program)} commands found")
    for command in command_to_parse:
        print_to_screen(command)


def sanitize_program(program):
    """Get tortoise program ready for interpretation.

    There are unnecessary characters like spaces and comments which we want to get rid of.
    If a command has two parts, the second element of the list will be an empty string.
    Remove this element. Then remove all elements after the first empty string in each list.
    These were the comments at the end of each command."""
    for command in program:
        if len(command) > 1:
            command.pop(1)
            if len(command) > 2:
                del command[command.index(" ") :]
    return program


def navigate_command_functions(commands, program):
    """For each command, call the corresponding function.

    Number each command of the tortoise program and call the
    correct function for each command to be interpreted."""
    command_to_parse = []
    pen_state = MOVE
    for i, command in enumerate(program, 1):
        result = commands[command[0]](command, pen_state)
        if isinstance(result, tuple):
            pen_state = result[1]
            result = result[0]
        command_to_parse.append(f"{i}. {result}")
    return command_to_parse


def pen_up(_, pen_state):
    """Interprets the 'pen up' command."""
    ignored = " (ignored)" if pen_state == MOVE else ""
    return f"PEN UP{ignored}", MOVE


def pen_down(_, pen_state):
    """Interprets the 'pen down' command."""
    ignored = " (ignored)" if pen_state == DRAW else ""
    return f"PEN DOWN{ignored}", DRAW


def pen_colour(command, _):
    """Selects a pen colour."""
    return f"P {command[1]}"


def move_north(command, pen_state):
    """Moves the pen north a certain distance in centimetres."""
    return format_direction_and_units(command, pen_state, "north")


def move_south(command, pen_state):
    """Moves the pen south a certain distance in centimetres."""
    return format_direction_and_units(command, pen_state, "south")


def move_east(command, pen_state):
    """Moves the pen east a certain distance in centimetres."""
    return format_direction_and_units(command, pen_state, "east")


def move_west(command, pen_state):
    """Moves the pen west a certain distance in centimetres."""
    return format_direction_and_units(command, pen_state, "west")


def format_string_for_singular_or_plural(command):
    """Depending on the distance in the command, we use either 'unit' or 'units'."""
    return "units" if int(command[1]) > 1 else "unit"


def format_direction_and_units(command, pen_state, direction):
    """Returns the final, completed sentence."""
    pluralized = format_string_for_singular_or_plural(command)
    return f"{pen_state} {command[1]} {pluralized} to the {direction}."
