'''
Rate limit public interface.

This module includes the decorator used to rate limit function invocations.
Additionally this module includes a naive retry strategy to be used in
conjunction with the rate limit decorator.
'''
from functools import wraps
from math import floor
import datetime
import time
import sys
import threading


class RateLimitDecorator(object):
    def __init__(self, calls=15, period=900, clock=datetime.datetime.now):
        self.clamped_calls =  calls
        self.period = datetime.timedelta(seconds=period)
        self.clock = clock

        self.last_reset = clock()
        self.num_calls = 0

        self.lock = threading.RLock()

    def allow(self):
        with self.lock:
            period_remaining = self.__period_remaining()

            if period_remaining <= datetime.timedelta(seconds=0):
                self.num_calls = 0
                self.last_reset = self.clock()

            self.num_calls += 1

            if self.num_calls > self.clamped_calls:
                return False
            return True

    def __period_remaining(self):
        elapsed = self.clock() - self.last_reset
        return self.period - elapsed