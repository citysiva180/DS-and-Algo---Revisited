class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a fixed size."""
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Generate a hash for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update existing key
                return
        self.table[index].append([key, value])  # Add new key-value pair

    def get(self, key):
        """Retrieve a value by its key."""
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    def display(self):
        """Display the contents of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Example usage
hash_table = HashTable(size=5)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)

print(hash_table.get("apple"))  # Output: 10
hash_table.display()
hash_table.delete("banana")
hash_table.display()
