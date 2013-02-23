__author__ = 'josh'
import binio


class RegionFile:
    def __init__(self):
        self.regionFile = binio.new("""
            ((1, t_byte, 'offset0'),
             (1, t_byte, 'offset1'),
             (1, t_byte, 'offset2'),
             (1, t_byte, 'sector_count')) * 1024,

            (4, t_int32, 'timestamp') * 1024,

            (4, t_int32, 'length'),
            (1, t_byte, 'compression_type'),
            (length-1, t_byte, 'compressed_data')
        """)

    def load(self, filename):
        with open(filename, 'rb') as anvil_file:
            return self.regionFile.read_struct(anvil_file)
