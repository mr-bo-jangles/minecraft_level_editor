import pynbt


class NBTFile:
    def __init__(self):
        pass

    def load(self, filename):
        """
        Loads a chunk file using pyNBT, then closes the file.
        :param filename: string with path to chunk file
        :return: NBTFile instance with the chunk data.
        """
        self.filename = filename
        with open(filename) as io:
            nbt = pynbt.NBTFile(io)
        self.nbt = nbt

    def save(self, value, filename=None):
        """
        Saves a chunk file using pyNBT, then closes the file
        :param value: dict containing the values of the NBTFile to save back.
        :param filename: string of the filename to save to, defaults to the same file as was opened with.
        """
        if filename is None:
            filename = self.filename
        nbt = pynbt.NBTFile(value=value)
        with open(filename, 'wb') as io:
            nbt.save(io)

    def pprint(self):
        return self.nbt.pretty(indent="2", indent_str=" ")