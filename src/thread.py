#!/usr/bin/env python3

"""thread.py: The threading manager file for the CarSoft project."""

__author__ = "Rhys Read"
__copyright__ = "Copyright 2019, Rhys Read"

import logging
import threading


class ThreadManager(object):
    instance = None

    def __init__(self):
        if ThreadManager.instance is not None:
            logging.warning('ThreadManager repeat instance occurrence. Please check as this is undesirable.')

        ThreadManager.instance = self
        self.__threads = []

    def add_task(self, task):
        pass

    def start(self):
        pass

    def stop(self):
        pass
