import ctypes
from pathlib import Path,PureWindowsPath

SPI_SETDESKWALLPAPER = 0x14 #20
SPIF_UPDATEINIFILE = 0x2 #2 forces instant update

dirName = r"C:/Users/kaden/Pictures/
image = "laydownRedheadgirl"
suffix = ".jpeg"

fullpath = Path(dirName, image).with_suffix(suffix)
path_on_windows = PureWindowsPath(fullpath)

ctypes.windll.user32.SystemParametersIngoW(SPI_SETDESKWALLPAPER,0, path_on_windows)