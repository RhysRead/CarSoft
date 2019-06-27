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

    def add_task(self, func, args: tuple, start=True):
        thread = threading.Thread(target=func, args=args, daemon=True)
        self.__threads.append(thread)
        if start:
            thread.start()
        return thread

    def check_threads(self, remove_complete=True):
        for thread in self.__threads:
            if not thread.is_alive() and remove_complete:
                self.__threads.remove(thread)

    def start(self):
        for thread in self.__threads:
            if not thread.is_alive():
                thread.start()

