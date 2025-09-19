## Learning goals

- Create scripts and functions in Blockly.

- Learn and practice some of the programming basics:

  - Distance measurement using laser ping sensor

  - Turning ON/OFF LED lights based on the distance

  - Playing an alarm sound based on the distance

## Software and Hardware

- BlocklyProp Solo; Activity Board and Parallax USB programming cable

- Laser ping sensor

- Speaker

# Programming 

- Create a script that:

  1.  Reads laser ping sensor data in centimeters every 500 milliseconds and assigns it to a variable (e.g., distance); please note that the sensor is connected to pin 15.

  2.  Prints distance in centimeters in the terminal with its unit (e.g., distance: 10 cm)

  3.  Makes decisions based on the distance according to the table below:

+-----+------------------------+--------------------------------------------------+
| No. | Conditions             | Do                                               |
+:===:+========================+==================================================+
| 1   | If distance ≥ 50 cm    | Nothing (LED and speaker are OFF)                |
|     |                        |                                                  |
|     |                        | &                                                |
|     |                        |                                                  |
|     |                        | Print("distance \> 50") in terminal              |
+-----+------------------------+--------------------------------------------------+
| 2   | If 25 ≤ distance \< 50 | LED connected to pin 26 blinks every 300 ms      |
|     |                        |                                                  |
|     |                        | &                                                |
|     |                        |                                                  |
|     |                        | Print("25 ≤ distance \< 50") in terminal         |
+-----+------------------------+--------------------------------------------------+
| 3   | If 10 ≤ distance \< 25 | LED connected to pin 26 blinks every 100 ms      |
|     |                        |                                                  |
|     |                        | &                                                |
|     |                        |                                                  |
|     |                        | Print("10 ≤ distance \< 25") in terminal         |
+-----+------------------------+--------------------------------------------------+
| 4   | If distance \< 10      | Keep the LED 26 ON                               |
|     |                        |                                                  |
|     |                        | &                                                |
|     |                        |                                                  |
|     |                        | Print("distance \< 10") in terminal              |
|     |                        |                                                  |
|     |                        | &                                                |
|     |                        |                                                  |
|     |                        | Play a sound (e.g., techloop.wav) with volume 10 |
+-----+------------------------+--------------------------------------------------+

- Save your code on your computer periodically.

> Submit your code saved as ***Lab5_YourInitials_DescriptiveName** (e.g., Lab5_AM_ping_speaker)*

- Submit your code saved as a \*.svg file.

# Instructions and hints

- The script should have two main blocks:

  - **Main block**

    - Run a function in a new processor to play music based on the distance. Please note that the function should repetitively check the distance and act accordingly. This will be similar to making LED ON/OFF in a new processor (check your code for that activity).

    - A continuous loop (use *repeat forever* block) to read the sensor data

      - Please note that the sensor is connected to **pin 15**.

> ![Graphical user interface, application Description automatically generated](media/image1.png)

- Print the distance in the terminal.

- Call a function that makes decisions based on the distance. You can call this function 'parking_assist'.

- Pause for 500 milliseconds.

- At the end of the loop, please clear the screen (use *Terminal clear screen* block)

<!-- -->

- **Your function block**, which

  - Makes decisions according to the above table.

  - Please note that you may want to make pin 26 low if the distance exceeds 50 cm.

Suggestion: First, make the LED blink based on the table. Once it works the way we expect, add playing music (alarm sound).

**[Play Music]{.underline}**

- Download techloop.wav from Canvas, or you can download a sound from this library:

<https://learn.parallax.com/support/reference/sound-library>

- Paste the music files (.wav) onto the SD card of the activity board.

- Sample code to play music:

![A screenshot of a computer Description automatically generated with medium confidence](media/image2.png)

**Useful resources**

Play Music

<https://learn.parallax.com/support/reference/sound-library>

Propeller BlocklyProp Block Reference

<https://learn.parallax.com/support/reference/propeller-blocklyprop-block-reference>

- [Parking Assist BlocklyProp Project](https://learn.parallax.com/tutorials/language/blocklyprop/parking-assist-blocklyprop-project)

- [BlocklyProp reference PING))) Distance block](https://learn.parallax.com/support/reference/propeller-blocklyprop-block-reference/sensor/ping-distance)

- [True Colors Interactive Art Project with the LaserPING](https://learn.parallax.com/tutorials/language/blocklyprop/true-colors-interactive-art-project-laserping?_ga=2.190621544.2124006356.1651625574-1264960940.1644374482&_gac=1.136970500.1650136028.EAIaIQobChMIqOio3KOZ9wIVl8LCBB1n3wq9EAAYASAAEgJZg_D_BwE)

- [PING))) Wiring & Example Code](https://learn.parallax.com/support/reference/propeller-blocklyprop-block-reference/sensor/ping-distance/ping-wiring-example)

- [Sound library](https://learn.parallax.com/support/reference/sound-library)
