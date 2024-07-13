#include <FastLED.h> // FastLED library should be installed

#define PIN 6            // pin where the to which the data line of the LED strip is connected
#define NUM_PIXELS 10    // number of LEDs on the strip
CRGB pixels[NUM_PIXELS]; // our pixels array used to control the strip

void setup()
{
    // initalize the LED strip
    FastLED.addLeds<NEOPIXEL, PIN>(pixels, NUM_PIXELS);

    // set brightness (a bit lower than max to save our eyes)
    FastLED.setBrightness(100); // (min: 0, max: 255)

    // clear previous data from the strip
    FastLED.clearData();

    // set colors for three first pixels on the strip
    pixels[0] = CRGB(100, 255, 0); // green
    pixels[1] = CRGB(0, 100, 255); // blue
    pixels[2] = CRGB(255, 0, 100); // pink

    // update the physical led strip
    FastLED.show();
}

void loop()
{
    // do nothing yet
}