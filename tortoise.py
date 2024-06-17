import sys


def main():
    VALID_ARGS = ['tiny.tortoise', 'medium.tortoise', 'large.tortoise']

    FILENAME = get_tortoise_file(sys.argv, VALID_ARGS)
    if not '.tortoise' in FILENAME:
        print(FILENAME)
        exit()

    content = get_file_content(FILENAME)
    for i in content:
        print(i, end='\n')


def get_tortoise_file(argv, VALID_ARGS):
    try:
        FILENAME = argv[1]
    except IndexError:
        return '\nPlease specify an argument on the command line\n'
    if not argv[1] in VALID_ARGS:
        return "\nThat's not an existing tortoise file\n"
    return FILENAME


def get_file_content(FILENAME):
    with open(FILENAME, 'r') as tortoise:
        tortoise_program = tortoise.readlines()
    content = []
    for i, line in enumerate(tortoise_program, 1):
        content.append(f'{i}. {line.strip()}')
    return content



if __name__ == '__main__':
    main()
