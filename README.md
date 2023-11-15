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
