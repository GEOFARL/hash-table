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

    round = 0
    while length >= (round * 4) + 4:
        # Get 32 bit number by adding sequentially 8 bits at a time
        k = input[(round * 4)]
        k |= input[(round * 4) + 1] << 8
        k |= input[(round * 4) + 2] << 16
        k |= input[(round * 4) + 3] << 24

        # Guarantee that our value is 100% only 32 bits
        k = ensureInt4Bytes(k)

        # Manipulating bits of our 32-bit k number
        k = ensureInt4Bytes(k * m)
        k ^= k >> 4
        k = ensureInt4Bytes(k * m)

        h = ensureInt4Bytes(h * m)
        h ^= k

        round += 1

    numOfLeftBits = length - (round * 4)
    if numOfLeftBits == 1:
        h ^= input[-1]
        h = ensureInt4Bytes(h * m)
    elif numOfLeftBits == 2:
        h ^= ensureInt4Bytes(input[-1] << 8)
    elif numOfLeftBits == 3:
        h ^= ensureInt4Bytes(input[-1] << 16)
