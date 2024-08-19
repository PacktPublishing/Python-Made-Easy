import sys
from cx_Freeze import setup, Executable
import uuid

# Generate a new GUID
guid_code = "{" + str(uuid.uuid4()).upper() + "}"

# Modify the following lines according to your program's details
exe = Executable(
    script='invaders3.py',
    base='Win32GUI',  # Use 'Win32GUI' for a GUI application or 'Console' for a console application
    icon='spaceicon.ico'  # Optional, specify if you have an icon
)

# Modify the following lines to add shortcut to start menu
shortcut_definition = [
    ("ProgramMenuShortcut",                   # Shortcut name
     "ProgramMenuFolder",                     # Start menu folder
     "Space Invaders",                        ####### Change to name of program
     "TARGETDIR",                             # Component_
     "[TARGETDIR]invaders3.exe",              ####### Rename invaders3.exe to match the executable of your program.
     None,                                    # Arguments
     "Your program description",              ####### Add a Description
     None,                                    # Hotkey
     None,                                    # Icon
     None,                                    # IconIndex
     None,                                    # ShowCmd
     "TARGETDIR")                             # WkDir
]

# cx_Freeze setup
setup(
    name='Space Invaders',  ##### Rename your program
    version='1.0',
    description='Description of your program',   ##### Add a description to your program
    executables=[exe],
    options={
        'build_exe': {
            'includes': ['pygame'],  ###### Add any additional modules your program requires
            'include_files': ['explosion.png',
                              'rocket.png',
                              'ufo.png']  ###### Add any additional files your program requires
        },
        'bdist_msi': {
            'upgrade_code': guid_code,  
            'add_to_path': False,
            'initial_target_dir': r'[ProgramFilesFolder]\Invaders', ###### Change invaders to point to install destination dir
            'data': {
                'Shortcut': shortcut_definition  
            }
        }
    }
)
