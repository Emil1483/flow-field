import sys
import os
import keyboard

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_prev_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def get_float(prompt, on_error='{0} is not a valid input, please try again'):
    error = False
    while True:
        try:
            user_input = input(prompt)
            # if the previous attempt resulted in error,
            # remove the error text and make it look like
            # no error ever took place
            if error:
                clear_prev_lines(2)
                print(prompt + user_input)
            return float(user_input)
        except ValueError:
            error = True
            # first, remove the input prompt
            clear_prev_lines(1)
            # show error text
            print(on_error.replace('{0}', user_input))


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{get_float("float: ")} is an awesome number 😸. Thank you.')
