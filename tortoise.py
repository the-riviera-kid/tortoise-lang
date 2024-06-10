import tortoise_interpreter

def main():
    FILENAME = 'tiny.tortoise'
    with open(FILENAME, 'r') as tiny_tortoise:
        program = tiny_tortoise.readlines()
    # Create a list of lists where each line of commands
    # from the program are in a list. Strip the new lines
    # to exclude them as elements in these lists. 
    # If the command has two parts, the second element of the list
    # becomes and empty string due to the space in the command.
    # Remove the second element. 
    program = [list(i.strip()) for i in program]
    for i in program:
        if len(i) > 1:
            i.pop(1)
    tortoise_interpreter.main_tortoise(program)


if __name__ == '__main__':
    main()
