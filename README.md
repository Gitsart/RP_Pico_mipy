# RP_Pico_mipy
Hands-On with Pico Microcontroller/SoC embedded with RP2040 chip having a dual core ARM Cortex-M0+ processor which can be clocked up-to 133MHz. Pico has 2MB Onboard flash memory, 246Kb S-RAM  and 28 programmable GPIO pins. The model used is without WiFi.
Pico can be used with both C and MicroPython. 
For programming in C refer through the pico SDK installation manual - getting started with pico: https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf
Detailed datasheet for hardware SoC and pinout diagram is included. Kindly refer for GPIO pin numbers & functions, operating conditions and other hardware details.

*Here we are programming the pico using MicroPython. For this:
1)Build the Micropython port for pico. Just download and install the MiPy firmware for Pico. Follow the next steps.
2)Download the UF2 file for pico model : www.micropython.org/downloads/
3)Connect pico as a USB storage device to our computer, by press and holding the bootselect button while connecting the pico to the PC USB port.
4)Copy the UF2 file to the pico storage.
5) The board will reboot now.
6) Install and open Thonny IDE : www.thonny.org
7)Choose the board raspberry pi pico in the Thonny editor.

All set to program the pico .
