# import modules:
import board
import neopixel  # neopixel.py should be in /lib
import time
import math

# define program constants
NUM_PIXELS = 9
COLOR = (255, 65, 0)
BREATH_IN_DURATION_SECONDS = 1.0 * 2
BREATH_OUT_DURATION_SECONDS = 3.0 * 2
GAMMA_CORRECTION = 2.8
MIN_BRIGHTNESS = 0.2
MAX_BRIGHTNESS = 1.0

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP0,
    NUM_PIXELS,
    brightness=0.0,
    auto_write=False
)

# turn the entire strip off initially:
pixels.fill(COLOR)
pixels.show()

def getGammaValue(i):
    """Calculate gamma corrected brightness."""
    return math.pow(i / 100, GAMMA_CORRECTION)

def getGammaValueInverted(i):
    """Calculate inverted gamma corrected brightness."""
    return 1 - math.pow((100 - i) / 100, GAMMA_CORRECTION)

# this loop runs forever, our program interaction lives in here:
while True:
    for i in range(0, 101):
        # calculate brightness with gamma correction
        brightness = MIN_BRIGHTNESS + (MAX_BRIGHTNESS - MIN_BRIGHTNESS) * getGammaValue(i)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(BREATH_IN_DURATION_SECONDS / 100)

    for i in range(100, -1, -1):
        # calculate brightness with gamma correction
        brightness = MIN_BRIGHTNESS + (MAX_BRIGHTNESS - MIN_BRIGHTNESS) * getGammaValueInverted(i)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(BREATH_OUT_DURATION_SECONDS / 100)