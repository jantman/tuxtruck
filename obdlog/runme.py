#!/usr/bin/env python

# TuxTruck obdlog application - main runnable script
# Time-stamp: "2009-08-11 10:18:21 jantman"
# $LastChangedRevision$
# $HeadURL$
#

from TuxTruck_OBDlog_Main import *

if __name__ == '__main__':
    """ 
    main method for the whole program. Calls everything to... do... everything!
    """
    app = TuxTruck_OBDlog_Main(parent=None)
    app.run()
