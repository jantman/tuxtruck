# TuxTruck_OBDlog_SunSPOT_Reader.py
#
# Time-stamp: "2009-08-11 10:33:19 jantman"
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

import threading
import time

class TuxTruck_OBDlog_SunSPOT_Reader(threading.Thread):
    """
    Class to read the output of the SunSPOT accelerometer

    """

    PORT = ""
    FILE = None
    Q = ""

    def __init__(self, parent, q):
        """
        Open the port, start reading and buffering.
        """
        print "init"
        self.PORT = parent.SUNSPOT_PORT
        self.Q = q
        threading.Thread.__init__(self)
        
    def run(self):
        """
        Start thread...
        """
        self.FILE = open(self.PORT, "r")
        while True:
            self.Q.append(line)
            time.sleep(0.1)
