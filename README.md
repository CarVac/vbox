# vbox

![Overview of pcb and hand clusters](/Pictures/overview.jpg)

![Angled view of hand clusters](/Pictures/angleview.jpg)

A rectangle controller for Melee with buttons arranged vertically instead of on a flat surface.

It's intended to be highly modular and configurable to fit different people's button layout preferences and hand sizes.

The left- and right-hand finger clusters and thumb clusters are mirror images of each other, with shared daughterboard PCBs, each side having single-sided layouts.

The switches used are Omron D2LS-21(20M), which are easy to hand-solder. The SMD JST PH connector was chosen for its low profile and ease of hand soldering.

Any switch location can be omitted if desired, and the housing printed with a blank where it would go.

The motherboard is designed to be as narrow as possible, with 4 JST connectors for button cluster daughterboards and one FFC connector for the USB-C breakout board.

It is derived from the [Rana Labs Tadpole](https://github.com/rana-sylvatica/rana-tadpole) motherboard but with extremely heavy layout changes.

# License

This project is licensed under the CERN Open Hardware License Version 2 - Strongly Reciprocal

This license:

* Allows use, reproduction, modification, distribution, and sale of the design
* Requires distribution under the same terms and attribution to the original designer(s)
* Does not grant trademark rights
* May be terminated for non-compliance


If you are distributing vboxes or derivatives, you must provide a way for the recipient to access the source files (this repository or your fork if you modify it).

All of these files are posted as-is. This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY, AND FITNESS FOR A PARTICULAR PURPOSE.

# BOM

## PCBs

* Motherboard (with SMT assembly)
* [QeRB](https://github.com/rana-sylvatica/rana-tadpole/tree/main/PCBs/Breakout%20Board%20(QuRB)) (with SMT assembly) (USB-C breakout)
* 2x finger daughterboards (for hand assembly)
* 2x thumb daughterboards (for hand assembly)

## Electrical Parts

* 20x (or more) Omron D2LS-21(20M) mouse switches
* 2x S6B-PH-SM4-TB 6-pin right-angle surface-mount JST PH
* 2x S10B-PH-SM4-TB 10-pin right-angle surface-mount JST PH
* 2x A06KR06KR26E152A 6-pin 6" JST KR (PH-compatible) cable assembly, reversed
* 2x A10KR10KR26E102A 10-pin 4" JST KR (PH-compatible) cable assembly, reversed
* 1x 12-pin 0.5mm pitch ribbon cable, Xmm long

## Printed Parts

The housings may be customized to include or omit different button locations. Adjust the python file (which uses Build123D) where it says `EDIT THESE TO REMOVE BUTTON HOLES` and run the file to generate new STLs.

Print as many keycaps as necessary.

* Left Finger Cluster Housing
* Right Finger Cluster Housing
* Left Thumb Cluster Housing
* Right Thumb Cluster Housing
* 17x (or more) Short Keycaps
* 3x (or more) Tall Keycaps

Housing TBD; there may be a non-folding version and a folding version.

# Using the Motherboard with Other Button Clusters

You can use the motherboard with other finger clusters as long as you design them properly. The motherboard JST pinout is listed following, according to standard OpenFrame1 button locations.

## Pinout

### Left Hand Fingers

1. GND
2. Upper Row Index Finger (optional, GPIO 11)
3. Upper Row Ring Finger (optional, GPIO 23)
4. Upper Row Pinky Finger (optional, GPIO 25)
5. L
6. Analog Stick Left
7. Analog Stick Down
8. Analog Stick Right
9. Upper Row Middle Finger (optional, GPIO 1)
10. Start

### Right Hand Fingers

1. GND
2. Right Hand Start (optional, GPIO 29)
3. R
4. B
5. Y
6. X
7. Lightshield
8. Z
9. Midshield
10. Analog Stick Up

### Left Hand Thumbs

1. GND
2. Modifier 5 (optional, GPIO 10) (mirrored location of C-Stick Right)
3. Modifier 4 (optional, GPIO 9) (mirrored location of C-Stick Up)
4. Modifier 3 (optional, GPIO 8) (mirrored location of C-Stick Left)
5. ModY (mirrored location of C-Stick Down)
6. ModX (mirrored location of A)

### Right Hand Thumbs

1. GND
2. C-Stick Right
3. C-Stick Down
4. A
5. C-Stick Left
6. C-Stick Up

## Modifications

You may use as many or as few buttons as you would like, but keep in mind that if you are intending this for melee you should at least populate the standard 20 OpenFrame1 buttons.

When the JSTs of the button clusters are mounted on the **top side of the outer edges** of the PCBs (as in the reference design) or the **bottom side of the inner edges** of the PCBs, the pinout should be the same as on the motherboard, and you must use "reversed" cable assemblies which map pin 1 to pin 1 and pin N to pin N.

When the JSTs of the button clusters are mounted on the **bottom side of the outer edges** of the PCBs or the **top side of the inner edges** of the PCBs, the pinout should be reversed relative to the motherboard (1 to 10 and 10 to 1 for the fingers, and 1 to 6 and 6 to 1 for the thumb clusters) and you must use "non-reversed" (they simply omit the word reversed) cable assemblies that connect pin 1 to pin N. The correct cable assemblies are listed below:

* 2x A06KR06KR26E152**B** 6-pin 6" JST KR (PH-compatible) cable assembly, ***non-reversed***
* 2x A10KR10KR26E102**B** 10-pin 4" JST KR (PH-compatible) cable assembly, ***non-reversed***
