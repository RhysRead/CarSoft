#!/usr/bin/env python3

"""main.py: The main file for the execution of the CarSoft project."""

__author__ = "Rhys Read"
__copyright__ = "Copyright 2019, Rhys Read"

import logging

from display import DisplayManager

logging.basicConfig(level=logging.DEBUG)


class Main(object):
    def __init__(self, display_manager: DisplayManager):
        self.__display_manager = display_manager

    def start(self):
        # Starting managers

        # Beginning display manager on main thread
        self.__display_manager.start()


if __name__ == '__main__':
    display = DisplayManager()
    main = Main(display)
    main.start()
