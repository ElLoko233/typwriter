#Module: typewriter

This module provides a function for printing out text in type writer manner

**Function:** typing(txt, text_speed=0.05)

    def typing(txt, text_speed=0.05): 

        for char in txt:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(text_speed)

            else:
                time.sleep(text_speed + 0.3)

        else:
            sys.stdout.write("\n")

*   txt: Argument for text that will be printed
*   print_speed: Specifies time taken to pause after each character is printed. An  extra 0.3s is added for after printing a "\n" newline character.