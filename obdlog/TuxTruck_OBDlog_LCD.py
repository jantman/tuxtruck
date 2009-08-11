# TuxTruck_OBDlog_LCD.py
#
# Time-stamp: "2009-08-11 18:52:39 jantman"
#
# +----------------------------------------------------------------------+
# | TuxTruck Project      http://tuxtruck.jasonantman.com                |
# +----------------------------------------------------------------------+
# | Copyright (c) 2009 Jason Antman.                                     |
# |                                                                      |
# | This program is free software; you can redistribute it and/or modify |
# | it under the terms of the GNU General Public License as published by |
# | the Free Software Foundation; either version 3 of the License, or    |
# | (at your option) any later version.                                  |
# |                                                                      |
# | This program is distributed in the hope that it will be useful,      |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of       |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        |
# | GNU General Public License for more details.                         |
# |                                                                      |
# | You should have received a copy of the GNU General Public License    |
# | along with this program; if not, write to:                           |
# |                                                                      |
# | Free Software Foundation, Inc.                                       |
# | 59 Temple Place - Suite 330                                          |
# | Boston, MA 02111-1307, USA.                                          |
# +----------------------------------------------------------------------+
# |Please use the above URL for bug reports and feature/support requests.|
# +----------------------------------------------------------------------+
# | Authors: Jason Antman <jason@jasonantman.com>                        |
# +----------------------------------------------------------------------+
# | $LastChangedRevision:: 5                                           $ |
# | $HeadURL:: http://svn.jasonantman.com/tuxtruck/obdlog/shell.py     $ |
# +----------------------------------------------------------------------+

import Queue, threading, time
from util.crystalfontz635usb import crystalfontz635usb as CF635USB

class TuxTruck_OBDlog_LCD(threading.Thread):
    """
    Control output to an LCD display.
    """

    PORT = ""
    Q = None
    DISPLAY = None

    def __init__(self, parent, q, port):
        """
        Perform preliminary init of all child classes, DB, etc.
        """
        self.PORT = port
        self.Q = q
        threading.Thread.__init__(self)

    def run():
        """
        Start the thread.
        """
        self.DISPLAY = CF635USB(None, self.PORT)

        while True:
            if len(self.Q) > 0:
                foo = self.Q.pop()
                # explode, write to LCD
                # self.DISPLAY.writeLineFromLeft(num, text)
                # time.sleep(display.WAIT_TIME)
            else:
                time.sleep(0.1)
