class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        h = 14695981039346656037
        for b in str(key).encode():
            h *= 1099511628211
            h ^= b
        return h

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # def hash_djb2(s):                                                                                                                                
        #     hash = 5381
        #     for x in s:
        #         hash = (( hash << 5) + hash) + ord(x)
        #     return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)
        ##Above worked with collisions..... revised code below
        index = self.hash_index(key)  # find the hash index
        node = self.storage[index]
        if node is None: 
            self.storage[index] = HashTableEntry(key, value)
        else:
            if node.key != key:  # if we aren't overwriting
                while node.next is not None:  # while we can keep going to the right
                    if node.key != key:  # if it, again, isn't overwriting
                        node = node.next  # keep going
                    else:
                        node.value = value  # assign the value
                if node.key == key:  # we found it, we are overwriting
                    node.value = value
                else:
                    # we are attaching it to the end
                    node.next = HashTableEntry(key, value)
            else:
                node.value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        # self.storage[index] = None
        ##Above worked with collisions..... revised code below
        if self.get(key) is not None:  # if we have the item we want to delete
            index = self.hash_index(key)
            node = self.storage[index]
            while node.next is not None:  # while we can continue to search
                if node.key == key:  # we have found it, so we skip over it
                    node.key = node.next.key
                    node.value = node.next.value
                    node.next = node.next.next
                    return
                else:
                    node = node.next  # keep searching
            if node.key == key:  # the last item
                node.key = None
                node.value = None
                node.next = None
        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        # if self.storage[index] == None:
        #     return None
        # else:
        #     return self.storage[index].value
        ##Above worked with collisions..... revised code below
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:  # while we have items to search through
            while node.next is not None:  # while we are not at the end
                if node.key == key:  # found it!
                    return node.value  # so, return it!
                else:
                    node = node.next  # keep going
            if node.key == key:
                return node.value  # found it (first item)
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        old = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for entry in old:
            if entry==None: continue
            else:
                self.put(entry.key, entry.value)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
