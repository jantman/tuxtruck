#!/usr/bin/env python
import time
from util.crystalfontz635usb import crystalfontz635usb as CF635USB
DISPLAY = CF635USB(None, "/dev/ttyUSB0")

DISPLAY.clearScreen()
time.sleep(DISPLAY.WAIT_TIME)

DISPLAY.setContrast(95)
time.sleep(DISPLAY.WAIT_TIME)
DISPLAY.setBacklight(50)
time.sleep(DISPLAY.WAIT_TIME)

DISPLAY.writeSplitLine(0, "12345", "678")
time.sleep(DISPLAY.WAIT_TIME)

DISPLAY.writeLineFromLeft(3, "FOOBARBAZ")
time.sleep(DISPLAY.WAIT_TIME)

DISPLAY.clearLED(2)
time.sleep(DISPLAY.WAIT_TIME)
