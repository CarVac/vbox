# vbox

A rectangle controller for Melee with buttons arranged vertically instead of on a flat surface.

It's intended to be highly modular and configurable.

The finger clusters and the thumb clusters will be mirror images of each other, with shared daughterboard PCBs, each side having single-sided layouts.

The switches will be Omron D2LS-21(20M), which are easy to hand-solder. A SMD connector will be chosen to be simple to hand-solder.

Any switch can be omitted if desired, and the housing printed with a cap over where it would go.

The motherboard will be as narrow as possible, with 4 connectors for button cluster daughterboards and one further connector for the USB-C breakout board.
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
* 2x finger daughterboards (for hand assembly)
* 2x thumb daughterboards (for hand assembly)

## Electrical Parts

* 20x (or more) Omron D2LS-21(20M) mouse switches
* 2x S6B-PH-SM4-TB 6-pin right-angle surface-mount JST PH
* 2x S10B-PH-SM4-TB 10-pin right-angle surface-mount JST PH
* 2x A06KR06KR26E152A 6-pin 6" JST KR (PH-compatible) cable assembly
* 2x A10KR10KR26E102A 10-pin 4" JST KR (PH-compatible) cable assembly

## Printed Parts

The housings may be customized to include or omit different button locations.

Print as many keycaps as necessary.

* Left Finger Cluster Housing
* Right Finger Cluster Housing
* Left Thumb Cluster Housing
* Right Thumb Cluster Housing
* 17x (or more) Short Keycaps
* 3x (or more) Tall Keycaps

Housing TBD; there may be a non-folding version and a folding version.
