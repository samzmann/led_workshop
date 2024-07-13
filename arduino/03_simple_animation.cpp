#include <FastLED.h> // FastLED library should be installed

#define PIN 6            // pin where the to which the data line of the LED strip is connected
#define NUM_PIXELS 10    // number of LEDs on the strip
#define INTERVAL_MS 1000 // interval in milliseconds

CRGB pixels[NUM_PIXELS];          // our pixels array used to control the strip
int pixel_on_index = 0;           // index of the currently lit pixel
unsigned long last_timestamp = 0; // last update timestamp

void setup()
{
    // initalize the LED strip
    FastLED.addLeds<NEOPIXEL, PIN>(pixels, NUM_PIXELS);

    // set brightness (a bit lower than max to save our eyes)
    FastLED.setBrightness(100); // (min: 0, max: 255)

    // clear data and turn the entire strip off
    FastLED.clearData();
    fill_solid(pixels, NUM_PIXELS, CRGB::Black);
    FastLED.show();
}

void loop()
{
    // check current time
    unsigned long now = millis();

    // if it's been more than "INTERVAL_MS" since the last update, do another one:
    if (now > last_timestamp + INTERVAL_MS)
    {
        // turn OFF the pixel that is currently on
        pixels[pixel_on_index] = CRGB::Black;

        // increment the value of pixel_on_index
        if (pixel_on_index < (NUM_PIXELS - 1))
        {
            pixel_on_index += 1;
        }
        else
        {
            pixel_on_index = 0;
        }

        // turn ON the new pixel that is currently on
        pixels[pixel_on_index] = CRGB::Red;

        // update the physical led strip:
        FastLED.show();

        // update the timestamp variable:
        last_timestamp = now;
    }
}