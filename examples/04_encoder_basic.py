# import modules:
import board
from encoder import Encoder # encoder.py should be in /lib

# create our Encoder object:
encoder = Encoder(
    board.GP16, # CLK pin
    board.GP17, # DT pin
    board.GP15, # SW pin
)

while True:

    # get the latest rotation value:
    rotation = encoder.updateRotation()

    # check rotation direction and do stuff with it:
    if rotation == "clockwise":
        print("clockwise")
    elif rotation == "couterclockwise":
        print("couterclockwise")

    # get the latest button press value:
    press = encoder.updatePress()

    # check press value and do stuff with it:
    if press == "pressed":
        print("pressed")
    elif press == "released":
        print("released")