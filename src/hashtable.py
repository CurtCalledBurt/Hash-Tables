# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


    def __str__(self):
        return f"({self.key}: {self.value})"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Takes an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        """ inserts a key-value pair into the hashtable. If the same key is inserted twice, the previous key-value pair is overwritten with the new value. """
        # get the hashed key modulo the capacity
        hash_val_mod = self._hash_mod(key)

        # check for hash collision
        if self.storage[hash_val_mod] is not None:
            current = self.storage[hash_val_mod]
            # check if there is only one element in the linked list
            if current.next is None:
                # check if the key is already in use
                if current.key == key:
                    # overwrite old value
                    current.value = value
                # if key not in use, create new key-value pair
                current.next = LinkedPair(key, value)
            # if the list is longer than 1, get to the end of the linked list
            else:
                while current:
                    # check if the key is already in use
                    if current.key == key:
                        # overwrite old value
                        current.value = value
                        # we overwrite in place of insertion, so we can end the while loop early
                        break
                    # when at the end of the list, set the next node to be the new key value pair
                    if current.next is None:
                        current.next = LinkedPair(key, value)
                        # set current to be the newly inserted key-value pair
                        current = current.next
                    # increment pointer
                    current = current.next

        # if no collision, store both the key and the value
        else:
            self.storage[hash_val_mod] = LinkedPair(key, value)


    def remove(self, key):
        """ Removes value associated with inputed key, prints an error if the key is not found """

        # get the hash val modulo the capacity
        hash_val_mod = self._hash_mod(key)
        # go through all elements in the storage space and check for the given key
        current = self.storage[hash_val_mod]
        # chech if there nothing there
        if current is None:
            print("Error: Key not found")
        # check if there is only one element in the storage space
        elif current.next is None:
            if current.key == key:
                self.storage[hash_val_mod] = None
            else:
                print("Error: Key not found")
        # if there are multiple elements, cycle through them
        else:
            prev = current
            found_key = False
            while current:
                # check if the key matches
                if current.key == key:
                    # set the key to found
                    found_key = True
                    # delete the key
                    prev.next = current.next
                # update pointers
                prev = current
                current = current.next
            # if key is not found in the loop, print and error
            if found_key == False:
                print("Error: Key not found")


    def retrieve(self, key):
        """ returns the value associated with the inputed key. If the inputed key does not exist, returns None """

        # get hash val modulo capacity
        hash_val_mod = self._hash_mod(key)
        # go through all elements and check for the given key
        current = self.storage[hash_val_mod]
        # check if there is nothing there
        if current is None:
            return None
        # check if there is only one element in the storage space
        elif current.next is None:
            if current.key == key:
                return current.value
            else:
                return None
        # if there are multiple elements, cycle through them
        else:
            while current:
                # check if key matches
                if current.key == key:
                    return current.value
                # update pointer
                current = current.next
            # if key is not found during the loop, return None
            return "if 3"


    def resize(self):
        """ doubles capacity of storage and rehashes every value into the new storage """
        old_storage = self.storage
        self.storage = [None] * 2 * self.capacity
        self.capacity = len(self.storage)

        for elem in old_storage:
            current = elem
            while current:
                self.insert(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
