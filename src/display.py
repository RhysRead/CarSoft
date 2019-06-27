#!/usr/bin/env python3

"""display.py: The display file for the CarSoft project."""

__author__ = "Rhys Read"
__copyright__ = "Copyright 2019, Rhys Read"

import logging
import tkinter as tk
from abc import ABC


class DisplayManager(object):
    def __init__(self):
        self.__root = tk.Tk()
        self.__main_frame = MainFrame(self.__root)

        self.__current_frame_class: tk.Frame = None

    def set_frame_class(self, frame):
        self.__current_frame_class.pack_forget()
        frame.pack()
        self.__current_frame_class = frame

    def start(self):
        self.set_frame_class(self.__main_frame)


class FrameClass(ABC):
    def __init__(self, root: tk.Tk):
        self.__frame = tk.Frame(root)
        self.__create()

    def pack(self):
        self.__frame.pack()

    def pack_forget(self):
        self.__frame.pack_forget()

    @abstractmethod
    def __create(self):
        pass


class MainFrame(FrameClass):
    def __init__(self, root: tk.Tk):
        super().__init__(root)

    def c