// import library
#include <FastLED.h>
#include <RoxMux.h>

#define PIN 6         // pin where the data line of the LED strip is connected
#define NUM_PIXELS 10 // number of LEDs on the strip

#define PIN_CLK 11 // CLK pin for the encoder
#define PIN_DT 12  // DT pin for the encoder
#define PIN_SW 13  // SW pin for the encoder button

CRGB pixels[NUM_PIXELS]; // our pixels array used to control the strip
int pixel_on_index = 0;  // index of the currently lit pixel
CRGB color_on;           // current color of the lit pixel

RoxEncoder encoder;
RoxButton button;

void setup()
{
    // initialize the LED strip
    FastLED.addLeds<NEOPIXEL, PIN>(pixels, NUM_PIXELS);

    // set brightness (a bit lower than max to save our eyes)
    FastLED.setBrightness(100); // (min: 0, max: 255)

    // clear data and turn the entire strip off
    FastLED.clearData();
    fill_solid(pixels, NUM_PIXELS, CRGB::Black);

    // turn on pixel 0 to a random color
    color_on = CRGB(random(0, 255), random(0, 255), random(0, 255));
    pixels[pixel_on_index] = color_on;
    FastLED.show();

    // initialize the encoder pins
    pinMode(PIN_CLK, INPUT);
    pinMode(PIN_DT, INPUT);
    pinMode(PIN_SW, INPUT_PULLUP);

    Serial.begin(9600);

    encoder.setTickSensitivity(1);
    button.begin();
}

void loop()
{
    // read pin values to update encoder:
    encoder.update(digitalRead(PIN_CLK), digitalRead(PIN_DT), 8, LOW);

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
        pixels[pixel_on_index] = color_on;

        // update the physical led strip:
        FastLED.show();
    }

    // update the button state
    button.update(digitalRead(PIN_SW), 8, LOW);

    // change color when encoder button is pressed:
    if (button.pressed())
    {
        // generate a new random RGB color:
        color_on = CRGB(random(0, 255), random(0, 255), random(0, 255));

        // or a random HSV color:
        // hsv2rgb_rainbow(CHSV(random(0, 255), 255, 255), color_on);

        // update the color of the pixel that is currently on
        pixels[pixel_on_index] = hsv_2_rgb_rainbow(CHSV(random(0, 255), 255, 255) color_on);

        // update the physical led strip:
        FastLED.show();
    }
}