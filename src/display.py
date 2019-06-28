#!/usr/bin/env python3

"""display.py: The display file for the CarSoft project."""

__author__ = "Rhys Read"
__copyright__ = "Copyright 2019, Rhys Read"

import logging
import tkinter as tk
import abc


class DisplayManager(object):
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.pack_propagate(0)
        self.__root.resizable(0, 0)

        self.__main_frame = MainFrame(self.__root)

        self.__current_frame_class: tk.Frame = None

    def set_frame_class(self, frame):
        if self.__current_frame_class is not None:
            self.__current_frame_class.pack_forget()
        frame.pack()  # Todo: Consider using fill and expand here for proper scaling
        self.__current_frame_class = frame

    def start(self):
        self.set_frame_class(self.__main_frame)
        self.__root.mainloop()


class FrameClass(abc.ABC):
    def __init__(self, root: tk.Tk):
        self._root = root
        self._frame = tk.Frame(self._root)
        self._create()

    def pack(self):
        self._frame.pack()

    def pack_forget(self):
        self._frame.pack_forget()

    @abc.abstractmethod
    def _create(self):
        pass


class MainFrame(FrameClass):
    def __init__(self, root: tk.Tk):
        super().__init__(root)

        self._root.geometry('600x600+0+0')
        self._geom = "{0}x{1}+0+0".format(
            self._root.winfo_screenwidth(), self._root.winfo_screenheight())
        self._full = False

    def _create(self):
        self.__label0 = tk.Label(self._frame,
                                 text='CarSoft.',
                                 font='Helvetica 20 bold',
                                 fg='Grey')
        self.__label0.grid(row=0, column=0)

        self.__button0 = tk.Button(self._frame,
                                   text='Toggle Fullscreen',
                                   font='Helvetica 17 bold',
                                   command=self.__toggle_full_screen,
                                   width='10',
                                   height='5')
        self.__button0.grid(row=1, column=0)

    def __toggle_full_screen(self):
        # Toggling fullscreen attribute
        self._full = not self._full
        self._root.attributes('-fullscreen', self._full)

        # Toggling window geometry
        geom = self._root.winfo_geometry()
        geom = geom.split('+')[0] + '+0+0'
        logging.info('Switching window size from {} to {}.'.format(geom, self._geom))
        self._root.geometry(self._geom)
        self._geom = geom
