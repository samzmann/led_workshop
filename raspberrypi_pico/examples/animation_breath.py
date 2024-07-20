# import modules:
import board
import neopixel  # neopixel.py should be in /lib
import time
import math

# define program constants
NUM_PIXELS = 9
COLOR = (255, 65, 0)
BREATH_IN_DURATION_SECONDS = 1.0
BREATH_OUT_DURATION_SECONDS = 5.0
GAMMA_CORRECTION = 2.8
MIN_BRIGHTNESS = 0.05
MAX_BRIGHTNESS = 1.0
STEPS = 500

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

def getValue(i):
    """Calculate linear brightness without gamma correction."""
    return i / STEPS

def getGammaValue(i):
    """Calculate gamma corrected brightness."""
    return math.pow(i / STEPS, GAMMA_CORRECTION)

def getGammaValueInverted(i):
    """Calculate inverted gamma corrected brightness."""
    return 1 - math.pow((STEPS - i) / STEPS, GAMMA_CORRECTION)

def easeInOutSine(x):
    """Easing function for smooth transitions."""
    return 0.5 * (1 - math.cos(math.pi * x))

# this loop runs forever, our program interaction lives in here:
while True:
    for i in range(0, STEPS + 1):
        # calculate brightness with gamma correction and easing
        eased_i = easeInOutSine(i / STEPS)
        brightness = MIN_BRIGHTNESS + (MAX_BRIGHTNESS - MIN_BRIGHTNESS) * getGammaValue(eased_i * STEPS)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(BREATH_IN_DURATION_SECONDS / STEPS)

    for i in range(STEPS, -1, -1):
        # calculate brightness with gamma correction and easing
        eased_i = easeInOutSine(i / STEPS)
        brightness = MIN_BRIGHTNESS + (MAX_BRIGHTNESS - MIN_BRIGHTNESS) * getValue(eased_i * STEPS)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(BREATH_OUT_DURATION_SECONDS / STEPS)