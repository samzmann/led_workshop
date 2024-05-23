# import modules:
import board
import time
import neopixel # neopixel.py should be in /lib
from encoder import Encoder # encoder.py should be in /lib

# define program constants
NUM_PIXELS = 9
COLOR_OFF = (0, 0 ,0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_MAGENTA = (255, 0, 255)
COLOR_ORANGE = (255, 165, 0)
COLOR_PURPLE = (128, 0, 128)
COLOR_PINK = (255, 192, 203)
COLORS = [
    COLOR_RED,
    COLOR_GREEN,
    COLOR_BLUE,
    COLOR_YELLOW,
    COLOR_CYAN,
    COLOR_MAGENTA,
    COLOR_ORANGE,
    COLOR_PURPLE,
    COLOR_PINK
]

# define program variables
pixel_on_index = 0
color_index = 0
color_on = COLORS[color_index]

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP0,
    NUM_PIXELS,
    brightness=0.3,
    auto_write=False
)

# create our Encoder object:
encoder = Encoder(
    board.GP16, # CLK pin
    board.GP17, # DT pin
    board.GP15, # SW pin
)

# reset the leds:
pixels.fill((0, 0, 0))
pixels[pixel_on_index] = COLORS[color_index]
pixels.show()

while True:

    # get the latest rotation value:
    rotation = encoder.updateRotation()

    if rotation != None:
        # turn OFF the pixel that is currently on
        pixels[pixel_on_index] = COLOR_OFF

        # increment or decrement pixel_on_index:
        if rotation == "clockwise":
            pixel_on_index += 1

            # wrap around if pixel_on_index is greater than NUM_PIXELS:
            if pixel_on_index >= NUM_PIXELS:
                pixel_on_index = 0

        elif rotation == "couterclockwise":
            pixel_on_index -= 1
            
            # wrap around if pixel_on_index is smaller than 0:
            if pixel_on_index < 0:
                pixel_on_index = NUM_PIXELS - 1

        # turn ON the new pixel that is currently on
        pixels[pixel_on_index] = COLORS[color_index]

        # update the physical led strip:
        pixels.show()

    # get the latest button press value:
    press = encoder.updatePress()

    # increment color_index when encoder button is pressed:
    if press == "pressed":
        color_index += 1
        # wrap around if color_index is greater than the length of the COLORS array:
        if color_index >= len(COLORS):
            color_index = 0

        # update the color of the pixel that is currently on
        pixels[pixel_on_index] = COLORS[color_index]

        # update the physical led strip:
        pixels.show()