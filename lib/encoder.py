import digitalio
import rotaryio

class Encoder():
    def __init__(self, clkPin, dtPin, swPin) -> None:

        # initialize rotary encoder
        self.encoder = rotaryio.IncrementalEncoder(clkPin, dtPin, divisor=2)
        self.prevRotaryVal = 0

        # initialize button
        self.button = digitalio.DigitalInOut(swPin)
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP
        self.prevButtonVal = None

    def updateRotation(self):
        if self.encoder.position is not self.prevRotaryVal:
            isRotatingClockwise = self.encoder.position > self.prevRotaryVal
            self.prevRotaryVal = self.encoder.position
            if isRotatingClockwise:
                return "clockwise"
            else:
                return "couterclockwise"
        
    def updatePress(self):
        if not self.button.value and self.prevButtonVal is None:
            self.prevButtonVal = "pressed"
            return "pressed"
        if self.button.value and self.prevButtonVal == "pressed":
            self.prevButtonVal = None
            return "released"