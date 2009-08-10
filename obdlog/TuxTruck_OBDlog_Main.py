#
# TuxTruck obdlog application - main class
# Time-stamp: "2009-08-10 16:57:02 jantman"
# $LastChangedRevision$
# $HeadURL$
#

import Queue, threading, datetime, os.path
from datetime import datetime

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


    def run(self):
        """
        Once init is finished, start logging...
        """
        # start the gps thread
        # start the obd thread
        
        # every self.DATA_INTERVAL seconds, write the data to the data sink
