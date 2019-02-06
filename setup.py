"""
Written by Ali Zahid Raja
6th Feb 2019

This File was used to make the executeables for the source code provided
it makes a folder with all the dependencies for a windows user who does not have python and/or tkinter with him

"""


import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'D:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Python36\tcl\tk8.6'

build_exe_options = {"packages": [], "include_files": ["tcl86t.dll", "tk86t.dll"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Any2AnyConvertor",
    author = 'Ali Zahid Raja',
    version = "1.01",
    publisher = 'AliZahidRaja',
    options={'build_exe': build_exe_options},
    description = "Program to make convert file extensions",
    executables = [Executable("source.py", base = base)]
)