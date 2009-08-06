#
# TuxTruck obdlog application - main class
# Time-stamp: "2009-08-05 16:47:04 jantman"
# $LastChangedRevision$
# $HeadURL$
#

import Queue

class TuxTruck_OBDlog_Main():
    """
    Master class that handles all OBD logging functions.

    """

    SERIAL_PORT = "/dev/ttyS0"
    DATA_INTERVAL = 3
    gpsQueue = None
    obdQueue = None
    gps = None # the TuxTruck_OBDlog_gpsd object
    obd = None # the TuxTruck_OBDlog_obd object

    def __init__(self, parent, serialPort):
        """
        Perform preliminary init of all child classes, DB, etc.
        """
        self.SERIAL_PORT = serialPort
        # make sure GPSd is running. init the gpsd class, make sure were getting data
        # connect to the OBD interface, init it, get some sample data
        # init the database or flat file, wherever we put our data

        # assuming both of those worked, return true/ok/whatever

    def run(self):
        """
        Once init is finished, start logging...
        """
        # start the gps thread
        # start the obd thread
        
        # every self.DATA_INTERVAL seconds, write the data to the data sink
