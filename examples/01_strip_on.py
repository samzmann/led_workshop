# import modules:
import board
import neopixel # neopixel.py should be in /lib

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP0,
    9,
    brightness=0.3,
    auto_write=False
)

# set color for the entire strip (red):
pixels.fill((255, 0, 0))

# update the physical led strip:
pixels.show()

# try other colors:
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
