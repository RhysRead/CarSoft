#!/usr/bin/env python3

"""main.py: The main file for the execution of the CarSoft project."""

__author__ = "Rhys Read"
__copyright__ = "Copyright 2019, Rhys Read"

import logging
import time

from display import DisplayManager
from thread import ThreadManager

logging.basicConfig(level=logging.DEBUG)


class Main(object):
    def __init__(self):
        self.__display_manager = DisplayManager()
        self.__thread_manager = ThreadManager()

        logging.info('All managers initialised.')

    def start(self):
        logging.info('Starting CarSoft...')

        # Starting managers
        self.__thread_manager.start()

        logging.info('Finished starting. Displaying window on main thread.')
        # Beginning display manager on main thread
        self.__display_manager.start()


if __name__ == '__main__':
    main = Main()
    main.start()
