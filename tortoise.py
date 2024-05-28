TORTOISE_FILE = 'tiny.tortoise'

def main():
    with open(TORTOISE_FILE, 'r') as tortoise_commands:
        tortoise_program = tortoise_commands.readlines()
        tortoise_commands.close()
    for i, line in enumerate(tortoise_program):
        print(f'{i+1}. {line.strip()}')

if __name__ == '__main__':
    main()