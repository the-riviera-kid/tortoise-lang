def main():
    FILENAME = 'tiny.tortoise'

    with open(FILENAME, 'r') as tiny_tortoise:
        tortoise_program = tiny_tortoise.readlines()

    for i, line in enumerate(tortoise_program, 1):
        print(f'{i}. {line.strip()}')


if __name__ == '__main__':
    main()
