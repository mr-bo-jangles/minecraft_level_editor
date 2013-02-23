import os
from decompress import RegionFile


def run():
    region_object = RegionFile()
    print region_object.load(os.path.join(
        '/', 'home', 'josh', '.minecraft', 'saves', 'Server World Redux', 'DIM1', 'region', 'r.0.0.mca'))