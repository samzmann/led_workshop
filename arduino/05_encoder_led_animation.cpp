#include <FastLED.h> // FastLED library should be installed
#include <RoxMux.h>  // RoxMux library should be installed

#define PIN 6         // pin where the data line of the LED strip is connected
#define NUM_PIXELS 10 // number of LEDs on the strip

#define PIN_CLK 4 // CLK pin for the encoder
#define PIN_DT 5  // DT pin for the encoder

CRGB pixels[NUM_PIXELS];          // our pixels array used to control the strip
int pixel_on_index = 0;           // index of the currently lit pixel
unsigned long last_timestamp = 0; // last update timestamp

RoxEncoder encoder;

void setup()
{
    // initialize the LED strip
    FastLED.addLeds<NEOPIXEL, PIN>(pixels, NUM_PIXELS);

    // set brightness (a bit lower than max to save our eyes)
    FastLED.setBrightness(100); // (min: 0, max: 255)

    // clear data and turn the entire strip off
    FastLED.clearData();
    fill_solid(pixels, NUM_PIXELS, CRGB::Black);
    pixels[pixel_on_index] = CRGB::Red;
    FastLED.show();

    // initialize the encoder pins
    pinMode(PIN_CLK, INPUT);
    pinMode(PIN_DT, INPUT);

    Serial.begin(9600);

    encoder.setTickSensitivity(1);
}

void loop()
{
    // read pin values to update encoder:
    encoder.update(digitalRead(PIN_CLK), digitalRead(PIN_DT), 5, LOW);

    // if encoder was rotated, update the LED strip:
    if (encoder.read())
    {
        // turn OFF the pixel that is currently on
        pixels[pixel_on_index] = CRGB::Black;

        // increment or decrement pixel_on_index:
        if (encoder.clockwise())
        {
            pixel_on_index += 1;

            // wrap around if pixel_on_index is greater than NUM_PIXELS:
            if (pixel_on_index >= NUM_PIXELS)
            {
                pixel_on_index = 0;
            }
        }
        else
        {
            pixel_on_index -= 1;

            // wrap around if pixel_on_index is smaller than 0:
            if (pixel_on_index < 0)
            {
                pixel_on_index = NUM_PIXELS - 1;
            }
        }

        // turn ON the new pixel that is currently on
        pixels[pixel_on_index] = CRGB::Red;

        // update the physical led strip:
        FastLED.show();
    }
}