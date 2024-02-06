
# Import the radio module
from microbit import *
import radio

# Set radio group
radio.on()  # Turn on radio communication
radio.config(group=1)  # Set radio group (can be any number, but must be the same on both MicroBits)

# Global variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_letter_index = 0
message = ""
in_letter_cycle_mode = False

# Functions for letter cycling and adding
def cycle_letter():
    global current_letter_index
    current_letter_index = (current_letter_index + 1) % len(alphabet)
    display.scroll(alphabet[current_letter_index])

def add_letter():
    global message
    message += alphabet[current_letter_index]
    display.scroll(message)

# Main loop
while True:
    if button_a.was_released() and button_b.was_released():  # Check for simultaneous button release
        in_letter_cycle_mode = not in_letter_cycle_mode
        display.clear()

    if in_letter_cycle_mode:
        if button_a.was_released():
            cycle_letter()
        elif button_b.was_released():
            cycle_letter(-1)  # Cycle backward
        elif pin_logo.is_touched():
            add_letter()
        elif button_a.was_released() and button_b.was_released():
            radio.send(message)  # Send the message
            message = ""  # Clear the message
            in_letter_cycle_mode = False
            display.clear()
