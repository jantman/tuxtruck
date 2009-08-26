#!/usr/bin/env python

# TuxTruck obdlog application - main runnable script
# Time-stamp: "2009-08-26 09:00:52 jantman"
# $LastChangedRevision$
# $HeadURL$
#

from TuxTruck_NetworkManager import *

if __name__ == '__main__':
    """ 
    main method for the whole program. Calls everything to... do... everything!
    """
    app = TuxTruck_NetworkManager(parent=None)
    app.run()
