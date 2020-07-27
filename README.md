#Module: typewriter

This module provides a function that prints out text in a typewriter manner

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

- text: Argument that will be printing to the terminal
- text_speed: Specifies the time taken to pause after printing each character