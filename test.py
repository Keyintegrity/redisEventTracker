# encoding: utf-8

__author__ = 'keeper'

from redisEventTracker import EventTracker

et = EventTracker( host='localhost', port=63790, db=0)

et.track_event('nonexistent')



