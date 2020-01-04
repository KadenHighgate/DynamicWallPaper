import ctypes
import glob
import threading
import time
from pathlib import Path,PureWindowsPath


class LocalImageChanger:

    SPI_SETDESKWALLPAPER = 0x14 #20
    SPIF_UPDATEINIFILE = 0x2 #2 forces instant update
    __change_rate = 30 #seconds
    __directory = ''
    __images  = []
    __index = 0
    def __init__(self):
        self.__change_rate = 30 #seconds
        self.__directory = "C:\\Users\\kaden\\Pictures\\EyeCandy\\"
        self.__images = []
        self.__index = 0

    def get_images_from_directory(self, directory):
        for f in glob.glob(directory + '*'):
            if '.jpg' in f or '.bmp' in f:
                self.__images.append(f)

    def set_backround_change_rate(self,seconds):
        self.__change_rate = seconds

    
    def set_background(self, image_path):
        fullpath = image_path
        ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER,0, fullpath, 0)
        self.iterate_through_backgrounds()

    def iterate_through_backgrounds(self):
        if self.__index < len(self.__images) - 1:
            self.__index += 1
        else:
           self. __index = 0

    def run_program(self):
        self.get_images_from_directory(self.__directory)
        self.set_backround_change_rate(10)

        # args = [self.__images[self.__index]]

        self.set_background(self.__images[self.__index])
        while True:
            time.sleep(self.__change_rate)
            self.set_background(self.__images[self.__index])


        # while True:
        #     timer = threading.Timer(self.__change_rate, self.set_background, args)

        #     if timer._is_stopped = True:
        #         timer.start()
        #     else:
        #         time.sleep(self.__change_rate)
        #         timer.cancel()


        
            

image_changer = LocalImageChanger()
image_changer.run_program()
