import rotaryio

class Encoder():
    def __init__(self, clkPin, dtPin) -> None:

        # initialize rotary encoder
        self.encoder = rotaryio.IncrementalEncoder(clkPin, dtPin, divisor=2)
        self.prev_rotary_val = 0

    def updateRotation(self):
        if self.encoder.position is not self.prev_rotary_val:
            isRotatingClockwise = self.encoder.position > self.prev_rotary_val
            self.prev_rotary_val = self.encoder.position
            if isRotatingClockwise:
                return "clockwise"
            else:
                return "counterclockwise"