# import modules:
import board
import random
import neopixel # neopixel.py should be in /lib
from encoder import Encoder # encoder.py should be in /lib

# function to generate a random RGB value:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# define program constants
NUM_PIXELS = 9
COLOR_OFF = (0, 0 ,0)

# define program variables
pixel_on_index = 0
color_on = random_color()

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP16,
    NUM_PIXELS,
    brightness=0.3,
    auto_write=False
)

# create our Encoder object:
encoder = Encoder(
    board.GP17, # CLK pin
    board.GP18, # DT pin
    board.GP19, # SW pin
)

# reset the leds:
pixels.fill((0, 0, 0))
pixels[pixel_on_index] = color_on
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

        elif rotation == "counterclockwise":
            pixel_on_index -= 1
            
            # wrap around if pixel_on_index is smaller than 0:
            if pixel_on_index < 0:
                pixel_on_index = NUM_PIXELS - 1

        # turn ON the new pixel that is currently on
        pixels[pixel_on_index] = color_on

        # update the physical led strip:
        pixels.show()

    # get the latest button press value:
    press = encoder.updatePress()

    # change color when encoder button is pressed:
    if press == "pressed":
        # generate a new random color:
        color_on = random_color()

        # update the color of the pixel that is currently on
        pixels[pixel_on_index] = color_on

        # update the physical led strip:
        pixels.show()