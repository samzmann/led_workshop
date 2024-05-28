# import modules:
import board
import neopixel # neopixel.py should be in /lib

# create pixels object:
pixels = neopixel.NeoPixel(
    board.GP16,
    9,
    brightness=0.3,
    auto_write=False
)

# set color for the entire strip (red):
pixels.fill((255, 0, 0))

# set colors for three first pixels on the strip:
pixels[0] = ((100, 255, 0)) # green
pixels[1] = ((0, 100, 255)) # blue
pixels[2] = ((255, 0, 100)) # pink

# update the physical led strip:
pixels.show()
