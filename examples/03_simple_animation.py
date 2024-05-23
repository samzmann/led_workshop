# import modules:
import board
import neopixel # neopixel.py should be in /lib
import time

# define program constants
NUM_PIXELS = 9
COLOR_ON = (255, 0 ,0)
COLOR_OFF = (0, 0 ,0)
INTERVAL_SECONDS = 1

# define program variables
pixel_on_index = 0
last_timestamp = time.monotonic()

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP0,
    NUM_PIXELS,
    brightness=0.3,
    auto_write=False
)

# turn the entire strip off:
pixels.fill((0, 0, 0))
pixels.show()

# this loop runs forever, our program interaction lives in here:
while True:

    # check current time
    now = time.monotonic()

    # if it's been more than "INTERVAL_SECONDS" since the last update, do another one:
    if now > last_timestamp + INTERVAL_SECONDS:
        # turn OFF the pixel that is currently on
        pixels[pixel_on_index] = COLOR_OFF

        # increment the value of pixel_on_index
        if pixel_on_index < (NUM_PIXELS - 1):
            pixel_on_index += 1
        else:
            pixel_on_index = 0

        # turn ON the new pixel that is currently on
        pixels[pixel_on_index] = COLOR_ON

        # update the physical led strip:
        pixels.show()

        # update the timestamp variable:
        last_timestamp = now