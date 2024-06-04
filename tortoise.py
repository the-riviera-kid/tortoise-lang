import sys


def main():
    
    try:
        FILENAME = sys.argv[1]
    except IndexError:
        print('\nYou have to specify what tortoise you want executed.\
              \nPlease add it as an argument on the command line.\n')
        return

    with open(FILENAME, 'r') as tortoise:
        tortoise_program = tortoise.readlines()

    for i, line in enumerate(tortoise_program, 1):
        print(f'{i}. {line.strip()}')


if __name__ == '__main__':
    main()
