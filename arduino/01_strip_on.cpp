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

    CRGB colorPredefined = CRGB::Red;     // uses predefined colors
    CRGB colorCustom = CRGB(255, 0, 255); // uses custom RGB value

    // set color for the entire strip
    fill_solid(pixels, NUM_PIXELS, colorPredefined);

    // update the physical led strip
    FastLED.show();
}

void loop()
{
    // do nothing yet
}