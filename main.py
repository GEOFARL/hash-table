from murmurHash2 import murmur2
from generate_random_phrase import generate_random_phrase

n = 25
max_length = 20
keys = [generate_random_phrase(max_length) for _ in range(n)]
dictionary = {murmur2(bytes(value, 'ascii')): value for value in keys}
for i in dictionary:
    print(f'{i}:{dictionary[i]}')

# print(generate_random_phrase(10))
# print(murmur2(b'hello'))
