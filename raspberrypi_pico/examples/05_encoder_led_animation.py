# import modules:
import board
import neopixel # neopixel.py should be in /lib
from encoder_simple import Encoder # encoder_simple.py should be in /lib

# define program constants
NUM_PIXELS = 9
COLOR_OFF = (0, 0 ,0)
COLOR_ON = (255, 0, 0)

# define program variables
pixel_on_index = 0

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
)

# reset the leds to their initial state:
pixels.fill((0, 0, 0))
pixels[pixel_on_index] = COLOR_ON
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
        pixels[pixel_on_index] = COLOR_O

        # update the physical led strip:
        pixels.show()