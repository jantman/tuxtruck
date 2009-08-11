# TuxTruck_Thread_Queue.py
#
# Time-stamp: "2009-08-10 17:57:29 jantman"
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

import collections

class TuxTruck_Thread_Queue():
    """
    Implements a revolving queue (collections.deque) for threads in TuxTruck.

    """

    q = None

    def __init__(self, maxLength):
        """
        Init the object.

        maxLength -- integer maximum length
        """
        self.q = collections.deque(maxlen=maxLength)

    def __len__(self):
        """
        Set value for len() builtin
        """
        return len(self.q)

    def append(self, val):
        """
        Append a value to (the right of) the deque.
        """
        self.q.append(val)

    def pop(self):
        """
        Pop a value from (the right of) the deque.
        Returns None if deque is empty!
        """
        if self.getLength() < 1:
            return None
        return self.q.pop()

    def getLength(self):
        """
        Get the length of the deque.
        """
        return len(self.q)
