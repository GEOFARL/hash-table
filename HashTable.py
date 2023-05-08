from murmurHash2 import murmur2


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, value):
        key = value[:20]  # get the first 20 characters as key
        hashval = murmur2(bytes(key, 'ascii'))
        index = hashval % self.size

        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, value):
        key = value[:20]
        hashval = murmur2(bytes(key, 'ascii'))
        index = hashval % self.size

        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None
