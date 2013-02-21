import os
from chunk import Chunk


def run():
    chunk_object = Chunk()
    chunk_object.load(os.path.join(
        '/', 'home', 'josh', '.minecraft', 'saves', 'Server World Redux', 'DIM1', 'region', 'r.0.0.mca'))
    print chunk_object.pprint()