import os
from cx_Freeze import setup, Executable

base = None
executables = [Executable("game.py", base=base)]
packages = ["idna"]
include_files = [os.path.join('game')]

options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files,
    },
}

setup(
    name="Breakout",
    options=options,
    version="1.0.0",
    description='<any description>',
    executables=executables
)
