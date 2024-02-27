## initialize the LED strip
pixel_pin = board.GP16
num_pixels = 6
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)

def onRotate(direction):
    print('on rotate', direction)

def onClick():
    print('on click')

encoder = RotaryEncoder(
    board.GP19,
    board.GP18,
    board.GP17,
    onRotate,
    onClick
)

pixels.fill((0,0,0))
pixels.show()

time.sleep(2)

## update the entire strip
pixels.fill((255,0,0))
pixels.show()

time.sleep(2)

## update a single pixel
pixels[0] = (255,255,0)
pixels.show()

while True:
    encoder.listenToRotation()