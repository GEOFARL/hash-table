def ensureInt4Bytes(input: int):
    pass


def murmur2(input: bytes):
    # m is used in the MurmurHash algorithm as a magic constant multiplier
    # value of 0x5bd1e995 was chosen because it is
    # a prime number with good bit diffusion properties
    m = 0x5bd1e995

    # number of bits to be shifted
    r = 24
    seed = 0

    length = len(input)
    hash = seed ^ length
