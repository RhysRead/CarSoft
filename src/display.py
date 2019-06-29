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
        # Initial geometry declaration
        self.base_geometry = '1000x800+0+0'
        self.__root.geometry(self.base_geometry)
        self.__root.attributes('-fullscreen', False)

        self.__main_frame = MainFrame(self.__root, self)

        self.__current_frame_class: tk.Frame = None

    def set_frame_class(self, frame):
        if self.__current_frame_class is not None:
            self.__current_frame_class.pack_forget()
        frame.pack()  # Todo: Consider using fill and expand here for proper scaling
        self.__current_frame_class = frame

    def get_frame_class(self):
        return self.__current_frame_class

    def start(self):
        self.set_frame_class(self.__main_frame)
        self.__root.mainloop()


class FrameClass(abc.ABC):
    def __init__(self, root: tk.Tk, display_manager: DisplayManager):
        self._root = root
        self._display_manager = display_manager
        self._frame = tk.Frame(self._root)
        self._create()

    def pack(self):
        self._frame.pack()

    def pack_forget(self):
        self._frame.pack_forget()

    def _load_main_frame(self):
        self._display_manager.set_frame_class(MainFrame(self._root, self._display_manager))

    @abc.abstractmethod
    def _create(self):
        pass


class MainFrame(FrameClass):
    def __init__(self, root: tk.Tk, display_manager: DisplayManager):
        super().__init__(root, display_manager)

        window_geometry = clean_geometry(self._root.winfo_geometry())

        if window_geometry == self._display_manager.base_geometry\
                or window_geometry == '1x1+0+0':
            self._geom = "{0}x{1}+0+0".format(
                self._root.winfo_screenwidth(), self._root.winfo_screenheight())
            self._full = False
        else:
            self._geom = self._display_manager.base_geometry
            self._full = True

    def _create(self):
        self.__label0 = tk.Label(self._frame,
                                 text='CarSoft.',
                                 font='Helvetica 20 bold',
                                 fg='Grey')
        self.__label0.grid(row=0, column=0, sticky=tk.W, padx=100)

        self.__button0 = tk.Button(self._frame,
                                   text='Toggle\nFullscreen',
                                   font='Helvetica 17 bold',
                                   command=self.__toggle_full_screen,
                                   width='10',
                                   height='5')
        self.__button0.grid(row=0, column=1, sticky=tk.E, padx=100)

        self.__button1 = tk.Button(self._frame,
                                   text='Live\nDisplay',
                                   font='Helvetica 17 bold',
                                   command=self.__load_live_display,  # Todo: Create live display
                                   width='10',
                                   height='5')
        self.__button1.grid(row=1, column=0, sticky=tk.E, padx=100)

        self.__button2 = tk.Button(self._frame,
                                   text='Media\nManager',
                                   font='Helvetica 17 bold',
                                   command=self.__load_media_manager,  # Todo: Create media manager
                                   width='10',
                                   height='5')
        self.__button2.grid(row=1, column=1, sticky=tk.E, padx=100)

        self.__button3 = tk.Button(self._frame,
                                   text='Config\nManager',
                                   font='Helvetica 17 bold',
                                   command=self.__load_config_manager,  # Todo: Create configuration manager
                                   width='10',
                                   height='5')
        self.__button3.grid(row=2, column=0, sticky=tk.E, padx=100)

        self.__button4 = tk.Button(self._frame,
                                   text='EXIT',
                                   font='Helvetica 17 bold',
                                   command=self._root.quit,
                                   width='10',
                                   height='5',
                                   fg='White',
                                   bg='Red')
        self.__button4.grid(row=2, column=1, sticky=tk.E, padx=100)

    def __load_live_display(self):
        self._display_manager.set_frame_class(LiveDisplayFrame(self._root, self._display_manager))

    def __load_media_manager(self):
        self._display_manager.set_frame_class(MediaManagerFrame(self._root, self._display_manager))

    def __load_config_manager(self):
        self._display_manager.set_frame_class(ConfigManagerFrame(self._root, self._display_manager))

    def __toggle_full_screen(self):
        # Toggling window geometry
        geom = self._root.winfo_geometry()
        # Replacing the position value of the window to fix a weird bug
        geom = clean_geometry(geom)
        logging.info('Switching window size from {} to {}.'.format(geom, self._geom))
        self._root.geometry(self._geom)
        self._geom = geom

        # Toggling fullscreen attribute
        self._full = not self._full
        self._root.attributes('-fullscreen', self._full)
        self._root.update()


class LiveDisplayFrame(FrameClass):
    def __init__(self, root: tk.Tk, display_manager: DisplayManager):
        super().__init__(root, display_manager)

    def _create(self):
        self.__button0 = tk.Button(self._frame,
                                   text='Main\nMenu',
                                   font='Helvetica 17 bold',
                                   command=self._load_main_frame,
                                   width='10',
                                   height='5')
        self.__button0.grid(row=0, column=0, sticky=tk.E, padx=100)

        self.__label0 = tk.Label(self._frame,
                                 text='0\nMPH',
                                 font='Helvetica 17 bold',
                                 fg='Red',
                                 width='10',
                                 height='5',
                                 bg='Grey')
        self.__label0.grid(row=1, column=0, sticky=tk.W, padx=100, pady=50)

        self.__label1 = tk.Label(self._frame,
                                 text='0\nRPM',
                                 font='Helvetica 17 bold',
                                 fg='Red',
                                 width='10',
                                 height='5',
                                 bg='Grey')
        self.__label1.grid(row=1, column=1, sticky=tk.W, padx=100, pady=50)


class MediaManagerFrame(FrameClass):
    def __init__(self, root: tk.Tk, display_manager: DisplayManager):
        super().__init__(root, display_manager)

    def _create(self):
        self.__button0 = tk.Button(self._frame,
                                   text='Main\nMenu',
                                   font='Helvetica 17 bold',
                                   command=self._load_main_frame,
                                   width='10',
                                   height='5')
        self.__button0.grid(row=0, column=1, sticky=tk.E, padx=100)


class ConfigManagerFrame(FrameClass):
    def __init__(self, root: tk.Tk, display_manager: DisplayManager):
        super().__init__(root, display_manager)

    def _create(self):
        self.__button0 = tk.Button(self._frame,
                                   text='Main\nMenu',
                                   font='Helvetica 17 bold',
                                   command=self._load_main_frame,
                                   width='10',
                                   height='5')
        self.__button0.grid(row=0, column=1, sticky=tk.E, padx=100)


def clean_geometry(geometry: str):
    """
    Removes the position value at the end of a geometry value.
    :param geometry:
    :return:
    """
    return geometry.split('+')[0] + '+0+0'
