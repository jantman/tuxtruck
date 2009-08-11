#!/usr/bin/env python
# writes a sample accelerometer data file to a named pipe
# for testing the accelerometer handling code

# FIRST run mkfifo /tmp/accelfifo

import time

FILE = open("accelData-out", "r")

LINES = []

for line in FILE:
    LINES.append(line)

FIFO = open("/tmp/accelfifo", "w+")

i = 0
while True:
    if i >= (len(LINES) - 1):
        i = 0
    FIFO.write(LINES[i])
    FIFO.flush()
    i = i + 1
    time.sleep(0.25)
