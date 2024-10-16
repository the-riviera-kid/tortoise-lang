"""Mini-language to control a simple turtle-graphics system."""

import tortoise_interpreter
import argparse



def main():
    """Read in a tortoise program to be interpreted."""

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="To specify the file you want to use on the program")
    parser.add_argument("-V", "--verbose", help="Increase output with filename and number of commands in file",
                        action="store_true")
    args = parser.parse_args()


    with open(args.filename, encoding="utf-8") as tortoise:
        program = tortoise.readlines()

    # Create a list of lists where each line of commands from the program are
    # in a list. Strip the new lines to exclude them as elements in these lists.
    program = [list(i.strip()) for i in program]
    tortoise_interpreter.main_tortoise(program, args)
    print()


if __name__ == "__main__":
    main()
