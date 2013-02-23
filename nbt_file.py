from cStringIO import StringIO
import pynbt


class NBTFile:
    def __init__(self):
        pass

    def load(self, nbt_data):
        """
        Loads a chunk file using pyNBT, then closes the file.
        :param filename: string with path to chunk file
        :return: NBTFile instance with the chunk data.
        """

        self.nbt = pynbt.NBTFile(nbt_data)

    def save(self, value):
        """
        Saves using pyNBT, then returns a cStringIO file containing the compressed NBT data
        :rtype : cStringIO, containing gzipped NBT data to be added back to data structure.
        :param value: dict containing the values of the NBTFile to save back.
        """
        io = StringIO()
        nbt = pynbt.NBTFile(value=value)
        nbt.save(io)
        return io

    def pprint(self):
        return self.nbt.pretty(indent="2", indent_str=" ")