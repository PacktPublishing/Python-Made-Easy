import sys
from cx_Freeze import setup, Executable

# Define the path to your main script
main_script = 'invaders3.py'

# Create the executable
executables = [Executable(script=main_script)]

# Define setup details
setup(
    name='SpaceInvaders',                                                # Name of the application
    version='1.0',                                                       # Version number
    description='Space Invaders Game',                                   # Description of the application
    options={
        'build_exe': {
            'packages': ['pygame'],                                      # Packages to include
            'include_files': ['rocket.png', 'ufo.png', 'explosion.png']  # Additional files to include
        }
    },
    executables=executables                                              # List of executables to create
)
