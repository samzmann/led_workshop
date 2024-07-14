#include <RoxMux.h>

#define PIN_CLK 11 // CLK pin for the encoder
#define PIN_DT 12  // DT pin for the encoder

RoxEncoder encoder;

void setup()
{
    pinMode(PIN_CLK, INPUT);
    pinMode(PIN_DT, INPUT);

    Serial.begin(9600);
}

void loop()
{

    // read pin values to update encoder:
    encoder.update(digitalRead(PIN_CLK), digitalRead(PIN_DT), 5, LOW);

    // if encder was rotated, print the direction:
    if (encoder.read())
    {
        if (encoder.clockwise())
        {
            Serial.println("Clockwise ");
        }
        else
        {
            Serial.println("Counter-Clockwise ");
        }
    }
}