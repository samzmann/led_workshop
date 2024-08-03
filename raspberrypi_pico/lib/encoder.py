import rotaryio
import digitalio
from adafruit_debouncer import Debouncer


class Encoder():
    def __init__(self, clkPin, dtPin, swPin) -> None:

        # initialize rotary encoder
        self.encoder = rotaryio.IncrementalEncoder(clkPin, dtPin, divisor=2)
        self.prev_rotary_val = 0

        # initialize button
        button_pin = digitalio.DigitalInOut(swPin)
        button_pin.direction = digitalio.Direction.INPUT
        button_pin.pull = digitalio.Pull.UP
        self.button = Debouncer(button_pin)


    def updateRotation(self):
        if self.encoder.position is not self.prev_rotary_val:
            isRotatingClockwise = self.encoder.position > self.prev_rotary_val
            self.prev_rotary_val = self.encoder.position
            if isRotatingClockwise:
                return "clockwise"
            else:
                return "counterclockwise"
        
    def updatePress(self):
        self.button.update()
        if self.button.fell:
            return "pressed"
        if self.button.rose:
            return "released"