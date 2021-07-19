import cx_Freeze

cx_Freeze.setup(
    name = "AtlasDesigner",
    version = "3.0.1",
    description = "Vector Graphics, Text Graphics, and Pixel Graphics Editor",
    executables = [cx_Freeze.Executable("Graphics Projects.py", base="Console")]
    )
