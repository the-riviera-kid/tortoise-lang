import sys
import tortoise_interpreter

def main():
    try:
        FILENAME = sys.argv[1]
    except IndexError:
        print('\nYou have to specify what tortoise you want executed.\
              \nPlease add it as an argument on the command line.\n')
        return
    
    with open(FILENAME, 'r') as tortoise:
        program = tortoise.readlines()
        
    # Create a list of lists where each line of commands from the program are
    # in a list. Strip the new lines to exclude them as elements in these lists. 
    program = [list(i.strip()) for i in program]
    tortoise_interpreter.main_tortoise(program)

if __name__ == '__main__':
    main()
