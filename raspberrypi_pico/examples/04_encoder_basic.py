# import modules:
import board
from encoder_simple import Encoder # encoder_simple.py should be in /lib

# create our Encoder object:
encoder = Encoder(
    board.GP17, # CLK pin
    board.GP18, # DT pin
)

while True:

    # get the latest rotation value:
    rotation = encoder.updateRotation()

    # check rotation direction and do stuff with it:
    if rotation == "clockwise":
        print("clockwise")
    elif rotation == "couterclockwise":
        print("couterclockwise")