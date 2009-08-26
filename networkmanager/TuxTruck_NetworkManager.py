# TuxTruck_NetworkManager.py
#
# Time-stamp: "2009-08-26 08:59:30 jantman"
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

import dbus
import time

class TuxTruck_NetworkManager():
    """
    Class to perform DBUS-based cotrol of NetworkManager.
    """

    PARENT = None
    BUS = None
    NM = None

    def __init__(self, parent):
        """
        Get the DBUS object and initialize things.
        """
        self.PARENT = parent
        self.BUS = dbus.SystemBus()
        self.NM = self.BUS.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager')
        
    def run(self):
        """
        DO the shit.
        """
        print "run()"
        print "STATE:"
        print self.NM.state()
        print "ACTIVE CONNECTIONS:"
        print self.NM.GetActiveConnections()
