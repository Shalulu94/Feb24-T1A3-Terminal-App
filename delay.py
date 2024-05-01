import time
import sys

# Delay print text
def print_pause(message):
    print(message)
    time.sleep(0.6)

# letter by letter delay
def print_delay(message):
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)