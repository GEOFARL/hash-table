from murmurHash2 import murmur2
from generate_random_phrase import generate_random_phrase
from HashTable import HashTable

n = 25
max_length = 20
keys = [generate_random_phrase(max_length) for _ in range(n)]

ht = HashTable(n // 3)
for key in keys:
    ht.insert(key)

print('Value:', keys[0])
print('From hash table:', ht.search(keys[0]))
print('')
print('Value:', keys[1])
print('From hash table:', ht.search(keys[1]))
