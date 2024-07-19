# import modules:
import board
import neopixel  # neopixel.py should be in /lib
import time
import math

# define program constants
NUM_PIXELS = 9
COLOR = (255, 0, 0)
INTERVAL_SECONDS = 0.01
GAMMA_CORRECTION = 2.8

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

# this loop runs forever, our program interaction lives in here:
while True:
    for i in range(0, 101):
        # calculate brightness with gamma correction
        brightness = math.pow(i / 100, GAMMA_CORRECTION)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(INTERVAL_SECONDS)

    for i in range(100, -1, -1):
        # calculate brightness with gamma correction
        brightness = math.pow(i / 100, GAMMA_CORRECTION)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(INTERVAL_SECONDS)