def main_tortoise(program):
    COMMANDS = {'U': pen_up, 'D': pen_down, 'P 3': pen_three}
    command_to_parse = navigate_command_functions(COMMANDS, program)
    for command in command_to_parse:
        print(command)


def navigate_command_functions(COMMANDS, program):
    return [f'{i}. {COMMANDS[command]()}' for i, command in enumerate(program, 1)]


def pen_up():
    return f'PEN UP'


def pen_down():
    return f'PEN DOWN'


def pen_three():
    return f'P 3'