This repository contains the example files for the LED strip (NeoPixel) workshop.
The examples are available for both Arduino and Raspberry Pi Pico and are located in these respective folders.

# Before you start

## For Arduino...

## For Raspberry Pi Pico...
- the device must be flashed with the CircuitPython bootloader
- copy the contents of the `/lib` directory onto the same folder on the device

# Summary of examples

## 01. Strip On
This very simple sketch initializes a LED strip, and turns the entire strip ON to the specified RGB color. A series of extra colors are available to try.

## 02. Individual Pixels
This sketch demonstrates how to turn on specific pixels on the strip.

## 03. Simple Animation
This sketch demonstrates how to animate the LED strip by turning on one pixel at a time in sequence, making use of the "main loop". The pixel turns off after a specified interval and the next pixel in the sequence turns on, creating a moving light effect.

## 04. Encoder Basic
This simple sketch iniitalizes an encoders. In the main loop is reads the value of the encoder and if a turn is dectected, it prints out the direction: clockwise or counterclockwise.

## 05. Encoder LED Animation
This sketch is a variant of example 03. Instead of using time to control the position of the lit LED, it uses an encoder. As you turn the encoder clockwise or counterclockwise, the lit LED moves up or down along the strip.

## 06. Encoder LED Button
This sketch builds upon example 05 by adding functionality for the button on the encoder module. When the button is pressed, the color of the currently lit LED changes to a random color.