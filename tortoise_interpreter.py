"""Implementation of tortoise-language."""


def main_tortoise(program, print_to_screen=print):
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
    return [
        f"{i}. {commands[command[0]](command)}" for i, command in enumerate(program, 1)
    ]


# fmt: off
def pen_up(_):
# fmt: on
    """Interprets the 'pen up' command."""
    return "PEN UP"


def pen_down(_):
    """Interprets the 'pen down' command."""
    return "PEN DOWN"


def pen_colour(command):
    """Selects a pen colour."""
    return f"P {command[1]}"


def move_north(command):
    """Moves the pen north a certain distance in centimetres."""
    return format_direction_and_units(command, "north")


def move_south(command):
    """Moves the pen south a certain distance in centimetres."""
    return format_direction_and_units(command, "south")


def move_east(command):
    """Moves the pen east a certain distance in centimetres."""
    return format_direction_and_units(command, "east")


def move_west(command):
    """Moves the pen west a certain distance in centimetres."""
    return format_direction_and_units(command, "west")


def format_string_for_singular_or_plural(command):
    """Depending on the distance in the command, we use either 'unit' or 'units'."""
    return 'units' if int(command[1]) > 1 else 'unit'


def format_direction_and_units(command, direction):
    """Returns the final, completed sentence."""
    return f"Move {command[1]} {format_string_for_singular_or_plural(command)} to the {direction}."
