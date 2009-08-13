# crystalfontz635usb.py Version 1.0
# Time-stamp: "2009-08-13 01:35:17 jantman"
# $Id: crystalfontz635usb.py,v 1.1 2009/03/29 05:30:51 jantman Exp $
# Class to control the CrystalFontz 635 USB display

# Copyright 2008 Jason Antman <http://www.jasonantman.com> <jason@jasonantman.com>
# THIS CLASS is licensed under the spirit of the GNU GPLv3.
# You may use, distribute, and modify it as much as you wish, with no restrictions, provided that:
# 1) You keep this copyright and license terms notice intact.
# 2) You keep the CVS Id line and the Version line intact, adding your own name/email and your own version number.
# 3) You keep these same license terms for your version, namely that it can be redistributed and modified without further restrictions.
# 4) !!!!!!!!!!!!! You send me a copy of your changes (via the e-mail address above) so I can include them in my next version.

import serial
import time
import sys
import struct
import string

# TODO: whenever there's empty bits at the end of data, it fails because the CRC is supposed to be packed in there.

class crystalfontz635usb:
    """
    This is a class to control the CrystalFOntz 635 USB display using PySerial. It should (eventually) implement all possible functionality, but currently just writes to the screen and controls the LEDs. WARNING: there usually needs to be a wait for response from the LCD. You have to deal with this.
    """

    # time to wait between commands
    WAIT_TIME = 0.1

    # character codes for builtin CGROM
    CHAR_DEGREES = 128 # superscript zero / degrees
    CHAR_RTN = 28 # the return symbol
    CHAR_FULL_BOX = 31 # fully colored box
    CHAR_ARRHEAD_L = 17 # arrowhead left
    CHAR_ARRHEAD_R = 16 # arrowhead right
    CHAR_ARRHEAD_UP = 26 # arrowhead up
    CHAR_ARRHEAD_DN = 27 # arrowhead down
    CHAR_PLUSMINUS = 140 # plus/minus sign
    CHAR_INF = 159 # infinity symbol?
    CHAR_STOP = 187 # a stop sign? a circle?
    CHAR_ARR_UP = 222 # arrow up
    CHAR_ARR_R = 223 # arrow right
    CHAR_ARR_DN = 224 # arrow down
    CHAR_ARR_L = 225 # arrow left
    # full-height bars
    CHAR_BAR_TALL_1 = 218
    CHAR_BAR_TALL_2 = 217
    CHAR_BAR_TALL_3 = 216
    CHAR_BAR_TALL_4 = 215
    CHAR_BAR_TALL_5 = 214
    # about half-height bars
    CHAR_BAR_1 = 212
    CHAR_BAR_2 = 211
    CHAR_BAR_3 = 210
    CHAR_BAR_4 = 209
    CHAR_BAR_5 = 208

    # cursor styles
    CURSOR_STYLE_NONE = 0
    CURSOR_STYLE_BLINK_BLOCK = 1
    CURSOR_STYLE_UNDERSCORE = 2
    CURSOR_STYLE_BLINK_BLOCK_UNDERSCORE = 3
    CURSOR_STYLE_BLINK_BLOCK_INVERTING = 4

    # suggested contrast values
    """
    Sets the contrast to an integer value from 0 (very light) to 255 (very dark).
    0-65     very light
    66       light
    95       about right
    125      dark
    126-255  very dark
    """

    CONTRAST_VERY_LIGHT = 63
    CONTRAST_LIGHT = 66
    CONTRAST_NORMAL = 95
    CONTRAST_DARK = 125
    CONTRAST_VERY_DARK = 200
    
    # lookup table for the CRCs
    crcLookupTable = [0x00000,0x01189,0x02312,0x0329B,0x04624,0x057AD,0x06536,0x074BF,0x08C48,0x09DC1,0x0AF5A,0x0BED3,0x0CA6C,0x0DBE5,0x0E97E,0x0F8F7,0x01081,0x00108,0x03393,0x0221A,0x056A5,0x0472C,0x075B7,0x0643E,0x09CC9,0x08D40,0x0BFDB,0x0AE52,0x0DAED,0x0CB64,0x0F9FF,0x0E876,0x02102,0x0308B,0x00210,0x01399,0x06726,0x076AF,0x04434,0x055BD,0x0AD4A,0x0BCC3,0x08E58,0x09FD1,0x0EB6E,0x0FAE7,0x0C87C,0x0D9F5,0x03183,0x0200A,0x01291,0x00318,0x077A7,0x0662E,0x054B5,0x0453C,0x0BDCB,0x0AC42,0x09ED9,0x08F50,0x0FBEF,0x0EA66,0x0D8FD,0x0C974,0x04204,0x0538D,0x06116,0x0709F,0x00420,0x015A9,0x02732,0x036BB,0x0CE4C,0x0DFC5,0x0ED5E,0x0FCD7,0x08868,0x099E1,0x0AB7A,0x0BAF3,0x05285,0x0430C,0x07197,0x0601E,0x014A1,0x00528,0x037B3,0x0263A,0x0DECD,0x0CF44,0x0FDDF,0x0EC56,0x098E9,0x08960,0x0BBFB,0x0AA72,0x06306,0x0728F,0x04014,0x0519D,0x02522,0x034AB,0x00630,0x017B9,0x0EF4E,0x0FEC7,0x0CC5C,0x0DDD5,0x0A96A,0x0B8E3,0x08A78,0x09BF1,0x07387,0x0620E,0x05095,0x0411C,0x035A3,0x0242A,0x016B1,0x00738,0x0FFCF,0x0EE46,0x0DCDD,0x0CD54,0x0B9EB,0x0A862,0x09AF9,0x08B70,0x08408,0x09581,0x0A71A,0x0B693,0x0C22C,0x0D3A5,0x0E13E,0x0F0B7,0x00840,0x019C9,0x02B52,0x03ADB,0x04E64,0x05FED,0x06D76,0x07CFF,0x09489,0x08500,0x0B79B,0x0A612,0x0D2AD,0x0C324,0x0F1BF,0x0E036,0x018C1,0x00948,0x03BD3,0x02A5A,0x05EE5,0x04F6C,0x07DF7,0x06C7E,0x0A50A,0x0B483,0x08618,0x09791,0x0E32E,0x0F2A7,0x0C03C,0x0D1B5,0x02942,0x038CB,0x00A50,0x01BD9,0x06F66,0x07EEF,0x04C74,0x05DFD,0x0B58B,0x0A402,0x09699,0x08710,0x0F3AF,0x0E226,0x0D0BD,0x0C134,0x039C3,0x0284A,0x01AD1,0x00B58,0x07FE7,0x06E6E,0x05CF5,0x04D7C,0x0C60C,0x0D785,0x0E51E,0x0F497,0x08028,0x091A1,0x0A33A,0x0B2B3,0x04A44,0x05BCD,0x06956,0x078DF,0x00C60,0x01DE9,0x02F72,0x03EFB,0x0D68D,0x0C704,0x0F59F,0x0E416,0x090A9,0x08120,0x0B3BB,0x0A232,0x05AC5,0x04B4C,0x079D7,0x0685E,0x01CE1,0x00D68,0x03FF3,0x02E7A,0x0E70E,0x0F687,0x0C41C,0x0D595,0x0A12A,0x0B0A3,0x08238,0x093B1,0x06B46,0x07ACF,0x04854,0x059DD,0x02D62,0x03CEB,0x00E70,0x01FF9,0x0F78F,0x0E606,0x0D49D,0x0C514,0x0B1AB,0x0A022,0x092B9,0x08330,0x07BC7,0x06A4E,0x058D5,0x0495C,0x03DE3,0x02C6A,0x01EF1,0x00F78]

    def __init__(self, parent, device):
        """
        Init function. Takes one real arg, device - the path to the tty. (Also takes parent, but that's to be assumed).
        @param parent (reference) - reference to parent, or None
        @param device (string) - the path to the device, i.e. "/dev/ttyUSB0"
        """
        # initiate a serial connection with 
	self.conn = serial.Serial(device, 115200)

    def getCRC(self, s):
        """
        Internal function to get the CRC of a given string prior to transmission.
        @param s (string) - the string
        """
	global crcLookupTable # we'll use the lookp table

	crcValue = 0x0FFFF # seed the CRC

	# calculate the CRC using the lookup table
	for ch in s:
	    crcValue = (crcValue >> 8) ^ self.crcLookupTable[((crcValue ^ ord(ch)) & 0xFF)]
	# now, all we need to do is invert the bits...
	return crcValue ^ 0xffff

    def sendCommand(self, command, data):
        """
        Low-level helper function. Just sends the specified command and data to the device.
        @param command (string) - the command to send
        @param data (string) - the data to send
        """

        # some commands with short data lengths have to be handled specially...
        if command == 0x0E:
            s = chr(0x0E)+chr(0x01)+data
            CRC = self.getCRC(s)
            CRCs = struct.pack("H", CRC)
            buffer = s+CRCs
        else:
            # make sure data is a string
            data = str(data)
            # struct format for the data - how many s'es?
            dataFmt = str(len(data))+"s"
            # length of the dat
            dataLen = len(data)
            # format for the final struct
            structFmt = "BB"+dataFmt+"H" # unsigned char command, unsigned char dataLen, char[] data, unsigned short crc
            # temporary struct to calculate the CRC
            temp = struct.pack("BB"+dataFmt, command, dataLen, data)
            # calculate the CRC itself
            CRC = self.getCRC(temp)
            # pack the whole thing into a struct called buffer
            buffer = struct.pack(structFmt, command, dataLen, data, CRC)

        # write the struct to the display
	self.conn.write(buffer)

    def writeLineFromLeft(self, lineNum, text):
	"""
	This function writes a line of text (param text) on the screen, on the line specified by lineNum. The text should be a string, maximum length of 20 chracters. If you want it centered, you should pad it yourself. lineNum should be an integer from 0 to 3.
        @param lineNum (int) - the line number, 0 to 3
        @param text (string) - the text to write (max len 20)
	"""
        self.sendCommand(0x1F, chr(0)+chr(lineNum)+string.ljust(text, 20))

    def writeCenteredLine(self, lineNum, text):
        """
        This function writes a line of text (param text), with the text centered on the line (line number specified by lineNum). The text should be a string, maximum length of 20 chracters. lineNum should be an integer from 0 to 3.
        @param lineNum (int) - the line number, 0 to 3
        @param text (string) - the text to write (max len 20)
        """
        self.writeLineFromLeft(lineNum, string.center(text, 20))

    def writeSplitLine(self, lineNum, leftText, rightText):
        """
        This function writes a line of text with the two text elements left and right justified, respectively, on the line (line number specified by lineNum). The text should be a string, maximum length of 20 chracters. lineNum should be an integer from 0 to 3.
        @param lineNum (int) - the line number, 0 to 3
        @param leftText (string) - text to left justify
        @param rightText (string) - text to right justify
        """
        foo = len(leftText) + len(rightText)
        if foo >= 20:
            bar = leftText + "|" + rightText
        else:
            baz = " " * (20 - foo)
            bar = leftText + baz + rightText
        self.writeLineFromLeft(lineNum, bar)
	    
    def clearAllLEDs(self):
        """
        Just calls clearLED for all LEDs 0-3
        """
        self.clearLED(0)
        # make sure it's done doing what it does before we do something else
        time.sleep(self.WAIT_TIME)
        self.clearLED(1)
        # make sure it's done doing what it does before we do something else
        time.sleep(self.WAIT_TIME)
        self.clearLED(2)
        # make sure it's done doing what it does before we do something else
        time.sleep(self.WAIT_TIME)
        self.clearLED(3)

    def clearLED(self, LEDnum):
        """
        Clear the LED with the given number (0-3). LED3 is on the bottom and LED0 is on the top.
        @param LEDnum (int) - 0 to 3
        """
        ledPins = {0: [11, 12], 1: [9, 10], 2: [7, 8], 3: [5, 6]}

        self.sendCommand(0x22, chr(ledPins[LEDnum][0])+chr(0)) # clear green
        # make sure it's done doing what it does before we do something else
        time.sleep(self.WAIT_TIME)
        self.sendCommand(0x22, chr(ledPins[LEDnum][1])+chr(0)) # clear red

    def setBacklight(self, level):
        """
        Sets the backlight on the LCD and keypad. Takes an integer value of brightness from 0 (off) to 100 (full on).
        @param level (int) 0 to 100
        """
        # TODO: here, the CRC should tack itself onto the unused data bits.....
        self.sendCommand(0x0E, chr(level))

    def setLED(self, LEDnum, color, level):
        """
        Set the LED with the given number (0 is top, 3 is bottom) to the given color. Colors are 0 for green or 1 for red. Level is brightness - 0 is low/off, 1-99 is regulr (duty cycle) brightness, 100 is high.
        @param LEDnum (int) - LED number 0 to 3
        @param color (int) - color 0 for green or 1 for red (you have to mix yourself)
        @param level (int) - should usually be around 50 to 99
        """
        ledPins = {0: 11, 1: 9, 2: 7, 3: 5}
        if color == 1:
            pin = ledPins[LEDnum]+1
        else:
            pin = ledPins[LEDnum]
        self.sendCommand(0x22, chr(pin)+chr(level))

    def clearScreen(self):
        """
        Just clears the screen.
        """
        self.sendCommand(0x06, "")

    def saveAsBootState(self):
        """
        Saves the current state as the boot-up state - i.e. the welcome screen. This includes the characters on the LCD, special character definitions, cursor position and style, contrast, backlight, key press & release masks, baud rate, and LED/GPO settings.
        """
        self.sendCommand(0x04, "")

    def setCursorStyle(self, style):
        """
        Sets the current cursor style. Style is an int 0-4
        @param style (int) - the style, 0 to 4
        """
        self.sendCommand(0x0C, chr(style))

    def setCursorPos(self, row, col):
        """
        Sets the current cursor position in rows (0-4) and columns (0-19).
        @param row (int) - row portion of cursor position
        @param col (int) - col portion of cursor position
        """
        self.sendCommand(0x0B, chr(row)+chr(col))

    def setContrast(self, value):
        """
        Sets the contrast to an integer value from 0 (very light) to 255 (very dark).
        0-65     very light
        66       light
        95       about right
        125      dark
        126-255  very dark
        @param value (int) - contrast calue 0 to 255
        """
        self.sendCommand(0x0D, chr(value))

    # TODO: how to implement key reporting (p. 17, cmd 0x17)
    # TODO: implement cmd 0x01, get HW & FW version
    # TODO: implement cmd 0x1E - read reporting & status


"""

TODO: Check return packets from all of these...

TODO: How to setup key listener?

TODO: Special character definitions for Tux.

LISTENER:
11 - 0x80 - Key Activity Report


"""
