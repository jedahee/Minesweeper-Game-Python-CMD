import sys
from cx_Freeze import setup, Executable
setup(name = "setup",
      version = "0.1",
      executables = [Executable("main.py")])
