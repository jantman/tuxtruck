# TuxTruck_OBDlog_Main.py
#
# Time-stamp: "2009-08-11 10:37:40 jantman"
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
# | $LastChangedRevision::                                             $ |
# | $HeadURL::                                                         $ |
# +----------------------------------------------------------------------+
#

import Queue, threading, datetime, os.path
from datetime import datetime
from TuxTruck_OBDlog_SunSPOT_Reader import TuxTruck_OBDlog_SunSPOT_Reader
from util.TuxTruck_Thread_Queue import TuxTruck_Thread_Queue

class TuxTruck_OBDlog_Main():
    """
    Master class that handles all OBD logging functions.

    """

    #
    # CONFIGURATION
    #
    ELMSCAN_PORT = "/dev/ttyS0" # path to the serial port for the ElmScan
    SUNSPOT_PORT = "/dev/ttyACM0" # path to the SunSPOT
    DATA_INTERVAL = 2.0 # interval at which to collect data, in seconds (float)
    DATA_FILE_NAME = "" # what to call the data file
    DATA_FILE_PATH = "/home/jantman/" # where to put the data file

    # Queues
    gpsQueue = None # queue for the GPSd data
    obdQueue = None # queue for the OBD data
    accelQueue = None # queue for the accelerometer (SunSPOT) data

    # data source objects
    gps = None # the TuxTruck_OBDlog_gpsd object
    obd = None # the TuxTruck_OBDlog_obd object
    accel = None # the TuxTruck_OBDlog_accel object

    def __init__(self, parent):
        """
        Perform preliminary init of all child classes, DB, etc.
        """
        
        # make sure GPSd is running. init the gpsd class, make sure were getting data
        # connect to the OBD interface, init it, get some sample data
        # init the database or flat file, wherever we put our data

        # assuming both of those worked, return true/ok/whatever

        # setup a filename for this data
        dt = datetime.now()
        s = dt.strftime("%Y-%m-%d_%H-%M-%S")
        self.DATA_FILE_NAME = "obdlog_" + s + ".csv"

        # set data path
        if self.DATA_FILE_PATH == "":
            self.DATA_FILE_PATH = os.path.expanduser("~")

        # intialize SunSPOT
        self.accelQueue = TuxTruck_Thread_Queue(3)
        self.accel = TuxTruck_OBDlog_SunSPOT_Reader(self, self.accelQueue)


    def run(self):
        """
        Once init is finished, start logging...
        """
        # start the gps thread
        # start the obd thread
        
        # start the accel thread
        self.accel.start()

        # every self.DATA_INTERVAL seconds, write the data to the data sink
        while 1:
            print self.accelQueue.pop()

