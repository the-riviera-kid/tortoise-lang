import tortoise_interpreter

def main():
    FILENAME = 'tiny.tortoise'
    with open(FILENAME, 'r') as tiny_tortoise:
        program = tiny_tortoise.readlines()
    program = [i.strip() for i in program]
    tortoise_interpreter.main_tortoise(program)


if __name__ == '__main__':
    main()
