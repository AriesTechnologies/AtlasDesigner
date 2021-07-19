# --- Version Class --- #

class _Version(object):
    def __init__(self, List):
        """Creates a new version"""

        assert not isinstance(List, str), "An item in the list is a string not a list!"
        assert len(List) >= 2, "Not a correctly formatted version!\nEx. ( \"Update 0.0.1 Gamma\", \"Created\", \"Dec 1 2019, 12:30 CST\")"

        self.__name = List[0]
        self.__info = List[1]
        
        if len(List) == 3:
            self.__time = List[2]
        else:
            self.__time = "N/A"

    @property
    def name(self):

        return self.__name

    @property
    def info(self):

        return self.__info

    @property
    def time(self):

        return self.__time

    @property
    def version(self):

        return f"{self.name}: {self.info}, {self.time}"
    

# --- Versions Class --- #

class Versions(object):
    def __init__(self, List=[]):

        self.__all_versions = [_Version(version) for version in List]
        self.__current = self.__all_versions[-1]
        del List

    @property
    def current(self):

        return self.__current.version

    def get_name(self, version=None):

        if version == None:
            version = self.__current
        return version.name

    def get_timestamp(self, version=None):
        
        if version == None:
            version = self.__current
        return version.time
            
    def search(self, search):

        return tuple(version.version for version in self.__all_versions if search in version.version)


__all__ = ("Versions")


if __name__ == "__main__":
    
    v = Versions((("0.0.1 Gamma","Created"), ("0.0.2 Gamma","Updated"), ("0.0.3 Gamma","Built"), ("0.1.0 Beta","Improved"), ("0.2.0 Beta","Released")))
    print(v.current, v.search("Gamma"), v.get_name(), v.get_timestamp(), sep="\n")
