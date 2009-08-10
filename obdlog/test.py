#!/usr/bin/env python

"""
import threading
import datetime
        
class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" % (self.getName(), now)
        
for i in range(2):
    t = ThreadClass()
    t.start()
"""

import collections

q = collections.deque(maxlen=3)
print q

q.appendleft("ONE")
print q
q.appendleft("TWO")
print q
q.appendleft("THREE")
print q
q.appendleft("FOUR")
print q

print q.popleft()
print q
print q.popleft()
print q
print q.popleft()
print q

print "======================\n"

q = collections.deque(maxlen=3)
print q

q.append("ONE")
print q
q.append("TWO")
print q
q.append("THREE")
print q
q.append("FOUR")
print q

print q.pop()
print q
print q.pop()
print q
print q.pop()
print q
