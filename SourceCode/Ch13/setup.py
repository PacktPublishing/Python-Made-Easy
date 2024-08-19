import sys
from cx_Freeze import setup, Executable

# Include necessary packages (add any additional packages your application requires)
packages = ["pygame"]

# Specify the Space Invaders main script
target_script = "invaders3.py"

# Create the executable
executables = [
    Executable(target_script, base=None)
]

# Set up the build options
build_options = {
    "packages": packages,
    "excludes": [],
    "include_files": [
        "rocket.png",
        "ufo.png",
        "explosion.png"
    ],
}

# Create the setup configuration
setup(
    name="Space Invaders",
    version="1.0",
    description="Space Invaders Game",
    options={"build_exe": build_options},
    executables=executables
)
