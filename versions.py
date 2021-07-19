from avm import Versions

versions = Versions((
        ("FU 0.0.1 Gamma", "Added basic startup", "N/A"),
        ("FU 0.0.2 Gamma", "Added resizing", "N/A"),
        ("FU 0.0.3 Gamma", "Added pixel and surface array functionality", "N/A"),
        ("IU 0.0.4 Gamma", "Bug fixes with array functionality that caused array to only record blue pixel colors", "N/A"),
        ("FU 0.0.5 Gamma", "Added manual message placement", "N/A"),
        ("FU 0.0.6 Gamma", "Added automatic message placement, removed manual placement", "N/A"),
        ("IU 0.0.7 Gamma", "Fixed bug with automatic message placement that caused the first word not to show", "N/A"),
        ("FU 0.0.8 Gamma", "Added input for image name and word to be used", "N/A"),
        ("FU 0.0.9 Gamma", "Added API notes, versions, etc", "N/A"),
        ("IU 0.1.0 Gamma", "Changed buttons that resized the image", "N/A"),
        ("FU 1.0.0 Beta", "Added AtlasDesigner Command Compiler", "N/A"),
        ("FU 1.0.1 Beta", "Removed pixelarray and surfarray functionality due to that it wasn't needed", "N/A"),
        ("IU 1.0.2 Beta", "Changed how the application fills the image with the words", "N/A"),
        ("FU 2.0.0 Beta", "Added the ability to increase and decrease text size", "N/A"),
        ("IU 2.1.0 Alpha", "Fixed crashing bug with increasing and decreasing text size", "N/A"),
        ("FU 3.0.0 Alpha", "Redesigned the entire program, improved speed, removed AtlasDesigner Command Compiler", "Feb 19 2019, 17:08 CST"),
        ("IU 3.0.1 Alpha", "Greatly improved color average accuracy, greatly improved speed, removed useless variables", "Feb 20 2019, 20:02 CST"),
        ("IU 3.0.2 Alpha", "Improved placement of text", "Jul 3 2019, 19:09 CST"),
        ))

del Versions
if __name__ == "__main__":
    print(versions.current)#, versions.search("IU"), sep="\n")

    
