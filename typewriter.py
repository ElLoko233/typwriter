# module that contains function for printing output in a similar pattern as type writer

import sys
import time


def typing(txt, text_speed=0.05):  # Ths function is a substitute of the print function
    """This function prints each character in a similar manner as a type writer machine does """

    for char in txt:  # Iterating through each character with some delay
        sys.stdout.write(char)
        sys.stdout.flush()

        # testing if a character is a newline
        if char != "\n":
            # if character is not a new line the speed of each character printed will be the one specified
            time.sleep(text_speed)

        else:
            # if character is a newline extra delay with be added to the specified value
            time.sleep(text_speed + 0.3)

    else:
        sys.stdout.write("\n")


# testing
if __name__ == "__main__":
    text = "Here is some text to test type writer function \nHere is some text to test type writer function \nHere is " \
           "some text to test type writer function \nHere is some text to test type writer function \nHere is some " \
           "text to test type writer function \nHere is some text to test type writer function"

    typing(text, 0.01)
